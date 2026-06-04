# research-microns-coreg-functional-em

**Mode**: research  ·  **Effort**: deep

## Request

> Using the MICrONS functional NWB at /data/microns-functional/ (pick any sub-17797 ses-*-scan-* NWB present on disk) plus the caveclient minnie65_public datastack table 'apl_functional_coreg_forward_v5', for the FIRST 20 ROIs in PlaneSegmentation1 of the NWB, look up their EM pt_root_id via (session, scan_idx, field, unit_id). Save /work/microns_coreg_sample.csv (columns: unit_id, pt_root_id, pt_position_x, pt_position_y, pt_position_z). If no MICrONS NWB is present, document the dandi download command in /work/notes.md and exit cleanly.

## Final summary

---

## Summary
The MICrONS NWB file exists at `/data/microns-functional/` but is only 51% downloaded (31.7 GB of 62.4 GB). A forensic HDF5 decode revealed the showstopper: the root group's directory index (B-tree + heap pointers) lives in an Object Header Continuation block at byte 62,420,876,816 — right in the missing half — making every subdirectory, including PlaneSegmentation1, completely inaccessible. Additionally, the sandbox is network-restricted, so the caveclient query cannot reach `global.daf-apis.com` even with a token. No ROI-to-EM mapping could be produced.

## What I did
- Confirmed NWB exists but is truncated; attempted HDF5 superblock patch (reflinked copy, patched EOF bytes 40–47 from 62.4→31.7 GB) — h5py then reported the exact inaccessible address (62,420,876,816).
- Manually decoded the HDF5 v0 superblock and root object header to pin down *why* the file is unreadable (continuation block in missing region).
- Confirmed sandbox has no outbound network (caveclient auth fails) and no stored CAVE token.
- Wrote **`/work/notes.md`** — full technical diagnosis + DANDI download command + CAVE token setup instructions.
- Wrote **`/work/run_coreg.py`** — complete end-to-end script (NWB parse → caveclient query → CSV save) ready to run once the two prerequisites are met.
- Wrote **`/work/microns_coreg_sample.csv`** — headers-only placeholder (`unit_id, pt_root_id, pt_position_x, pt_position_y, pt_position_z`).

## Caveats / next steps
1. **Complete the download:** `dandi download "DANDI:000402/0.240430.2138" --output-dir /data/microns-functional/` (or resume the partial file with `--existing refresh`).
2. **Add CAVE token** to `~/.cloudvolume/secrets/cave-secret.json` before running `run_coreg.py`.
3. `run_coreg.py` parses `field` from the ImagingPlane name/location — if the MICrONS NWB stores this differently, a small tweak may be needed after inspecting the actual structure.
