
notes_md = """\
# MICrONS Functional Co-registration — Run Notes
*Generated: 2026-06-04*

## Status: BLOCKED — NWB file incomplete, sandbox network-restricted

### Files on disk
| Path | Actual size | Expected size | Completeness |
|------|-------------|---------------|-------------|
| `/data/microns-functional/sub-17797_ses-4-scan-9_behavior+image+ophys.nwb` | 31.7 GB | 62.4 GB | **51%** |

### Why the NWB can't be read
The NWB file uses HDF5 v0 superblock.  
The **root group Object Header** (at byte 96) contains a single message:  
→ `type=0x0010` (Object Header Continuation) pointing to **byte 62,420,876,816**.  
That address is beyond the truncated EOF (31,708,938,240 bytes).  
The continuation block (184 bytes) holds the Symbol Table message, which provides the
B-tree + local-heap addresses needed to enumerate *any* subdirectory.  
No amount of patching or `swmr` tricks will work — the structural index is simply
not present on disk.

### Why caveclient can't be queried
The sandbox container is **network-restricted** (no outbound internet).  
Even if a token were present, no connection can be established to
`global.daf-apis.com`.

---

## Fix 1 — Complete the DANDI download

The NWB comes from DANDI archive 000402 (dandiset version 0.240430.2138).

```bash
# Install dandi CLI (once)
pip install dandi

# Re-download / resume the specific NWB
dandi download \\
  "https://dandiarchive.org/dandiset/000402/0.240430.2138/assets/fbf48497-5d56-4a22-b9ae-f4dec8f79bbe" \\
  --output-dir /data/microns-functional/

# Alternatively, download the entire dandiset (large)
dandi download "DANDI:000402/0.240430.2138" --output-dir /data/microns-functional/
```

The canonical DANDI asset path for this NWB is:
`sub-17797/sub-17797_ses-4-scan-9_behavior+image+ophys.nwb`

---

## Fix 2 — Set a CAVE auth token (required for caveclient)

```python
import caveclient
client = caveclient.CAVEclient()
client.auth.save_token(token="<YOUR_TOKEN_HERE>")
# Token is stored at ~/.cloudvolume/secrets/cave-secret.json
```

Obtain a token from: https://global.daf-apis.com/sticky_auth/api/v1/

---

## Full working script (run after fixes above)

See `/work/run_coreg.py` for the end-to-end script.

---

## Technical context
- Session 4, scan 9 → decoded from filename `ses-4-scan-9`
- Table `apl_functional_coreg_forward_v5` on `minnie65_public` datastack maps
  `(session, scan_idx, field, unit_id)` → `(pt_root_id, pt_position_x/y/z)`
- PlaneSegmentation1 unit_ids in the NWB are stored in the `.id` dataset of the
  `processing/ophys/ImageSegmentation/PlaneSegmentation1` group
"""

with open("/work/notes.md", "w") as f:
    f.write(notes_md)
print("Wrote /work/notes.md")
