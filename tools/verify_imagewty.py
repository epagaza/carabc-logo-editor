#!/usr/bin/env python3
"""Read-only, independently implemented IMAGEWTY bootlogo verifier.

Usage: python tools/verify_imagewty.py ORIGINAL.img MODIFIED.img
No firmwares are modified by this script. Third-party firmware compatibility
cannot be certified by an offline structural comparison.
"""
from __future__ import annotations
import argparse
import hashlib
import struct
import sys
from pathlib import Path


def u32(data: bytes, offset: int) -> int:
    return struct.unpack_from('<I', data, offset)[0]


def ascii_field(data: bytes, start: int, count: int) -> str:
    return data[start:start+count].split(b'\x00', 1)[0].decode('ascii', 'replace')


def checksum(data: bytes) -> int:
    total=0
    for offset in range(0,len(data)-len(data)%4,4):
        total=(total+int.from_bytes(data[offset:offset+4],'little'))&0xffffffff
    remainder=data[len(data)-len(data)%4:]
    if remainder: total=(total+int.from_bytes(remainder,'little'))&0xffffffff
    return total


def jpeg_profile(data: bytes):
    if len(data)<20 or data[:2]!=b'\xff\xd8' or data[-2:]!=b'\xff\xd9':
        raise ValueError('No complete JPEG SOI/EOI')
    cursor=2; profile=None
    while cursor<len(data)-4:
        if data[cursor]!=0xff: raise ValueError('Invalid JPEG segment marker')
        while cursor<len(data) and data[cursor]==0xff: cursor+=1
        marker=data[cursor]; cursor+=1
        if marker==0xda: break
        if marker==1 or 0xd0<=marker<=0xd7: continue
        if cursor+2>len(data): raise ValueError('Truncated JPEG')
        size=int.from_bytes(data[cursor:cursor+2],'big')
        if size<2 or cursor+size>len(data): raise ValueError('Invalid JPEG segment size')
        if 0xc0<=marker<=0xcf and marker not in (0xc4,0xc8,0xcc):
            if marker!=0xc0 or profile is not None: raise ValueError('Unsupported JPEG SOF')
            if size<17 or data[cursor+2]!=8 or data[cursor+7]!=3: raise ValueError('Unsupported JPEG precision or components')
            height=int.from_bytes(data[cursor+3:cursor+5],'big')
            width=int.from_bytes(data[cursor+5:cursor+7],'big')
            samplings=tuple(data[cursor+9+i*3] for i in range(3))
            profile=(width,height,samplings)
        cursor+=size
    if profile is None: raise ValueError('Baseline JPEG profile not found')
    return profile


def read_container(raw:bytes):
    if raw[:8]!=b'IMAGEWTY' or len(raw)<1024: raise ValueError('Not IMAGEWTY')
    version=u32(raw,8)
    if version not in (0x300,0x403): raise ValueError(f'Unsupported IMAGEWTY {version:#x}')
    stride=u32(raw,0x38); count=u32(raw,0x3c)
    if stride!=1024 or not 1<=count<=300 or 1024+count*stride>len(raw): raise ValueError('Entry table invalid')
    table_end=1024+count*stride
    entries=[]
    for i in range(count):
        h=1024+i*stride
        if u32(raw,h+4)!=1024: raise ValueError('Entry header size invalid')
        subtype=ascii_field(raw,h+16,16)
        e={'index':i,'hdr':h,'type':ascii_field(raw,h+8,8),'subtype':subtype,'base':subtype.rstrip('0'),'name':ascii_field(raw,h+36,256),'capacity':u32(raw,h+0x124),'length':u32(raw,h+0x12c),'offset':u32(raw,h+0x134)}
        if e['length']>e['capacity'] or e['capacity']==0 or e['offset']<table_end or e['offset']%512 or e['offset']+e['capacity']>len(raw): raise ValueError(f'Invalid bounds at entry {i}')
        entries.append(e)
    ordered=sorted(entries,key=lambda e:e['offset'])
    if any(a['offset']+a['capacity']>b['offset'] for a,b in zip(ordered,ordered[1:])): raise ValueError('Overlapping IMAGEWTY components')
    logos=[e for e in entries if e['base']=='BOOTLOGO_FEX']
    if len(logos)!=1: raise ValueError('Wrong number of BOOTLOGO_FEX components')
    logo=logos[0]
    if logo['index']+1==count: raise ValueError('VBOOTLOGO_FEX missing')
    verify=entries[logo['index']+1]
    if verify['base']!='VBOOTLOGO_FEX' or verify['length']!=4: raise ValueError('Invalid VBOOTLOGO_FEX')
    image=raw[logo['offset']:logo['offset']+logo['length']]
    profile=jpeg_profile(image)
    if any(raw[logo['offset']+logo['length']:logo['offset']+logo['capacity']]): raise ValueError('Unexpected data in padding')
    checks=[]
    for a,b in zip(entries,entries[1:]):
        if b['base']=='V'+a['base'] and b['length']==4:
            actual=u32(raw,b['offset']); expected=checksum(raw[a['offset']:a['offset']+a['length']]);checks.append((a['name'],actual==expected))
    if not checks or not any(x[0]==logo['name'] for x in checks) or not all(ok for _,ok in checks): raise ValueError('Partition checksum invalid')
    return version,entries,logo,verify,checks,profile


def compare(a:bytes,b:bytes):
    ainfo=read_container(a);binfo=read_container(b)
    av,ae,al,ac,checks_a,profile_a=ainfo
    bv,be,bl,bc,checks_b,profile_b=binfo
    if len(a)!=len(b) or av!=bv or len(ae)!=len(be) or al['offset']!=bl['offset'] or al['capacity']!=bl['capacity'] or ac['offset']!=bc['offset'] or profile_a!=profile_b:
        raise ValueError('Different firmware layout or JPEG profiles')
    for original,updated in zip(ae,be):
        for name in ('hdr','type','subtype','name','offset','capacity'):
            if original[name]!=updated[name]: raise ValueError(f'Entry metadata differs at {original["index"]}: {name}')
        if original['index']!=al['index'] and original['length']!=updated['length']: raise ValueError('Unexpected entry length change')
    allowed=[(al['offset'],al['offset']+al['capacity']), (al['hdr']+0x12c,al['hdr']+0x130),(ac['offset'],ac['offset']+4)]
    changed=0
    for i,(x,y) in enumerate(zip(a,b)):
        if x!=y:
            changed+=1
            if not any(start<=i<end for start,end in allowed): raise ValueError(f'Unexpected firmware modification at 0x{i:X}')
    if changed==0: raise ValueError('Images identical: no modified logo found')
    return {'changed_bytes':changed,'size':len(a),'version':hex(av),'entries':len(ae),'checksums':len(checks_a),'jpeg_profile':profile_a,'original_sha256':hashlib.sha256(a).hexdigest(),'custom_sha256':hashlib.sha256(b).hexdigest()}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('original',type=Path);p.add_argument('custom',type=Path)
    args=p.parse_args()
    try:
        a=args.original.read_bytes();b=args.custom.read_bytes()
        if len(a)>536870912 or len(b)>536870912: raise ValueError('Firmware too large')
        r=compare(a,b)
    except (OSError,ValueError,struct.error) as err:
        print('FAIL:',err,file=sys.stderr)
        return 1
    print('PASS: static IMAGEWTY verification (NOT a guarantee of device compatibility)')
    for key,value in r.items(): print(f'{key}: {value}')
    return 0

if __name__=='__main__': raise SystemExit(main())
