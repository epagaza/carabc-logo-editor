# Carabc Logo Editor v1.0.0 — Community Edition

**Created by Eduardo Pagaza** · Copyright © 2026 Eduardo Pagaza

A free, self-contained, **offline** HTML editor for changing the **static startup logo only** in supported Allwinner IMAGEWTY firmware containers. The original firmware is never overwritten. This tool does **not** install firmware on a device.

**Languages:** English by default; español and 简体中文 available from the globe menu. **Appearance:** Dark by default; Light mode also available. Preferences are stored locally when permitted by the browser.

## Use

1. Extract the ZIP, then open `Carabc_Logo_Editor_v1.0.0.html` in an up-to-date Chromium-based browser (Chrome or Edge recommended). No server or network is required.
2. In **Load Firmware**, select an unmodified official `.img` supplied for your **exact device and hardware revision**.
3. In **Customize Logo**, choose a JPG, PNG, BMP or WebP. Compose it on a 1280×720 canvas or the firmware's original logo dimensions: fit mode, 10–200% scale, alignment, X/Y offsets, and solid-color/gradient/image background. Transparent areas are flattened into an opaque JPEG.
4. Click **Preview result**. Inspect the *actual encoded JPEG*, including compression. You must run this check again after changing composition settings.
5. In **Review & Save**, read and accept the warnings. Choose the output `.img` name **once** when generating: via the native Save As dialog when available, otherwise the editor's filename prompt. Do not overwrite the original file.
6. Use **Verify Firmware** to compare your downloaded customized `.img` against the original; save the comparison report.
7. Read **Next steps** for backup and compatibility precautions. Installation requires separate, device-specific manufacturer instructions and tools, which this editor does not provide.

**Background tip:** A background already baked into an opaque JPG cannot be removed by selecting a different background. To see a color behind dark artwork, use a transparent PNG. Complex background images can exceed the boot-logo byte capacity; generation will be blocked if the replacement fails size/profile checks.

## Safety and compatibility

- The application analyzes IMAGEWTY `0x300` and `0x403` variants with a supported table layout. Recognition of a container is **not** proof that a device can boot it.
- All changes are limited to the boot-logo image, the recorded logo length, and its verification checksum. Other firmware components must remain byte-identical.
- The replacement JPEG must match the original baseline JPEG dimensions and color sampling. Browsers that cannot produce a matching encoding cannot generate a replacement for that firmware.
- One owner-reported physical installation succeeded with Carabc HW601/DB601, firmware V1.49, `txw38S0-nogps`. This **does not certify** other devices or revisions. See [Known compatibility](KNOWN_COMPATIBILITY.md) and [Safety and limitations](SAFETY_AND_COMPATIBILITY.md).
- **Do not install** a firmware on an unconfirmed hardware revision. Even a passing structural check cannot guarantee a successful installation, startup, or recovery.

## Contents

| File | Purpose |
| --- | --- |
| `Carabc_Logo_Editor_v1.0.0.html` | Complete offline application |
| `README.es.md` / `README.zh-CN.md` | Spanish and simplified Chinese guides |
| `KNOWN_COMPATIBILITY.md` | Evidence and scope of compatibility |
| `SAFETY_AND_COMPATIBILITY.md` | Risks, validation rules, privacy, distribution |
| `tools/verify_imagewty.py` | Optional independent read-only Python 3 comparator: `python tools/verify_imagewty.py ORIGINAL.img CUSTOM.img` |
| `TEST_REPORT_v1.0.0.md` | Verification results and untested conditions |
| `CHANGELOG.md` | Public version history |
| `LICENSE` | MIT license for original code |

**Independent community project. Not affiliated with, endorsed by, or officially supported by Carabc, Allwinner, BMW or their respective manufacturers.** The license covers the project's original code and documentation; it does not grant permission to redistribute third-party firmware, artwork, drivers or flashing tools. None of those are bundled.