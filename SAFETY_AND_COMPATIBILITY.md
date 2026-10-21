# Safety, security, and verification limitations

1. **Offline only:** This application runs entirely in the browser and does not connect to a device or install firmware. No upload, analytics, third-party script, or network dependency is included.
2. **Keep the original:** Always preserve a separate, untouched copy of the official firmware supplied for the exact hardware model and revision. Do not use firmware for another display, board, or GPS variant.
3. **Supported structures:** The IMAGEWTY parser accepts the recognized `0x300/0x403` layouts, checks table integrity and component bounds, recognizes the `BOOTLOGO_FEX` payload and `VBOOTLOGO_FEX` verification entry, and checks supported checksums.
4. **Image profile:** The output must be a three-component baseline JPEG matching the original boot-logo dimensions and subsampling. If the browser cannot encode a matching JPEG or fit the data into the reserved region, generation must fail rather than patch an incompatible image.
5. **Changes permitted:** Only the allocated boot-logo content (with zero padding), the 32-bit logo logical-length field, and the corresponding verification checksum. Every other part of the output must be binary-identical to the input.
6. **Independent verification:** The Verify Firmware tab and `tools/verify_imagewty.py` check the original and modified files. These static checks **do not emulate the target hardware or guarantee compatibility**.
7. **No guarantees:** A valid `.img` may fail to install or boot, and recovery is not guaranteed. Loss of power, interrupted transfers, vendor signatures and differences in hardware are beyond the editor’s tests.
8. **Distribution:** Manufacturer firmware, private or customized firmware, trademark-protected artwork, USB drivers, and third-party flashing software are **not included**. The MIT license is limited to the original code/documentation here and does not grant rights over third-party material.

If you lack a device-specific installation and recovery procedure, **do not attempt to flash** based solely on this editor's output.