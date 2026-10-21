# Carabc Logo Editor v1.0.0 — Test Report

**Status:** v1.0.0 candidate, **not yet publicly released**. Awaiting the project owner's final acceptance in Windows.

**Date:** October 21, 2026  
**Owner / credits:** Eduardo Pagaza

## Changes verified

- Layout: X/Y offsets now have responsive field widths and labels above their values, avoiding translation-related overflow.
- Position controls: increased clearance between nine-point alignment and Reset / Center buttons.
- Review & Save: a short brand-neutral compatibility warning replaces the old third-party flashing-program reference.
- About: version 1.0.0, creator credit, and independent-project / no-affiliation disclaimer only.
- Internal v3.x Beta labels have been replaced in the user-facing interface by public v1.0.0 naming.

## Round 1 — User interface / browser testing

- JavaScript syntax passed `node --check`.
- Chromium functional runs succeeded with English, Spanish, simplified Chinese, Dark/Light themes and Next Steps.
- Layout checked across **18 combinations** (six viewport widths: 360, 560, 760, 1024, 1280, 1600 pixels; three languages). No horizontal overflow; the offset input fields stay inside the placement panel and there is **23 px** clearance before placement action buttons.
- End-to-end flow: local original firmware → logo → JPEG preflight → Review & Save → customized download → Verify Firmware → final step.
- Live/encoded preview closes and reopens; changing placement invalidates the prepared preview and prevents saving until preflight reruns.
- Save validation: cancel operation, reserved Windows filename, Unicode filename, and one native file-save-picker invocation **simulated** in Chromium.
- Invalid firmware was rejected; no browser JavaScript page errors or external network requests were observed in the tested flows.

## Round 2 — Independent firmware comparison / regression

- Known HW601 V1.49 original was processed with the approved JPEG and default composition. Generated output was **byte-identical** to the private reference firmware previously installed successfully by the owner.
- Separate read-only `tools/verify_imagewty.py` confirmed IMAGEWTY `0x300`, 39 entries, **7 valid checksums**, and **0 changes outside allowed BOOTLOGO regions**.
- A transparent PNG with white background / scale 60% generated successfully and independently verified.
- Structural regression using `IMAGEWTY 0x403` generated and independently verified.
- A previously corrupted input was correctly rejected.

## Scope and limitations

- This is **static** firmware verification, not proof of safe installation on other devices.
- **No new device flash** was performed for this release candidate. One owner-reported successful hardware installation belongs to the same known firmware family, not to every compatible-looking device.
- Native Windows Save As and preference persistence when reopening the actual local HTML file (`file://`) remain for the owner's **manual Windows acceptance**. The native picker was tested with a simulation, not a real Windows shell dialog.
- Final GitHub release and public visibility **require explicit owner authorization** after acceptance.
- No proprietary firmware, branding images, USB drivers, or third-party flashing executables are included in the public package.