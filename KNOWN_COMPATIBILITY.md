# Known compatibility — Carabc Logo Editor v1.0.0

The information below distinguishes **structural format support** from **owner-reported hardware success**.

| Evidence | Scope |
| --- | --- |
| Physical successful installation reported by project owner | Carabc HW601 / DB601 motorcycle display, firmware V1.49, `txw38S0-nogps`, February 2026, static startup JPEG |
| Analyzed offline and regression-tested | Supported IMAGEWTY `0x300` and `0x403` layouts, including associated checksums and replacement JPEG constraints |
| Not demonstrated | Compatibility with other hardware revisions, other vendor products, different GPS variants, and every device using IMAGEWTY |

The editor recognizes the owner's tested unmodified original firmware using an **exact SHA-256 fingerprint**, not a filename similarity. A matching hash identifies only that known *firmware file*, not the exact physical device connected to the user. The application has no device-detection or device-writing capability.

**Never treat “structure verified” as proof of safe flashing or successful startup.** Each user must obtain the appropriate original firmware for their own device and independently establish the manufacturer's installation and recovery procedure.
