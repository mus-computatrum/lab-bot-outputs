# Run `a537f0f3fe15` — research

**When (UTC):** 2026-06-04 04:59:05
**Datasets:** `abo-visualcoding-v1`

## Request

> [bench:research-abo-v1-sst-osi] Using the Allen Brain Observatory (Visual Coding 2P) cache at /data/abo-visualcoding-v1/, enumerate ophys experiments where targeted_structures includes 'VISp' AND cre_lines includes 'Sst-IRES-Cre'. For each session, compute the drifting-grating Orientation Selectivity Index (OSI) per cell. Save /work/abo_v1_sst_osi.csv (columns: ophys_experiment_id, cell_specimen_id, osi) plus a histogram at /work/abo_v1_sst_osi_hist.png. If the AllenSDK pre-fetched NWBs aren't present on disk, just pick the first 5 V1 + Sst-Cre experiments and let AllenSDK fetch them lazily.

## Summary

All done! Here's the final report:

## Summary
Loaded all 29 Allen Brain Observatory Visual Coding 2P NWBs from `/data/abo-visualcoding-v1/`, identified **11 experiments** carrying both `VISp` targeted structure and `Sst-IRES-Cre` genotype with a drifting-gratings stimulus block. Computed baseline-subtracted mean DF/F per trial, then OSI = (R_pref − R_orth) / (R_pref + R_orth) at each cell's preferred temporal frequency. Across **110 Sst cells** (108 valid), median OSI = **0.59**, mean = **0.61** — consistent with SST interneurons being moderately but not sharply tuned.

## What I did
- Scanned all 29 NWBs via h5py (`general/subject/genotype`, `general/targeted_structure`, `stimulus/presentation` keys) — AllenSDK import is broken in sandbox (missing `SimpleITK`, `requests_toolbelt`), so worked entirely in h5py.
- Confirmed 11 VISp + Sst-IRES-Cre NWBs had drifting-gratings block (the other 18 were Session B/C2 types, which only have natural movies / static gratings).
- For each NWB: extracted DF/F traces (n_cells × n_frames), cell specimen IDs, and stimulus trial table (8 orientations × 5 TFs, ~60-frame trials at ~30 Hz).
- Computed per-trial baseline-subtracted responses (30-frame pre-stimulus window), averaged by (orientation, TF), and derived OSI at preferred TF.
- **Saved:** `/work/abo_v1_sst_osi.csv` (110 rows × 3 cols: `ophys_experiment_id`, `cell_specimen_id`, `osi`) and `/work/abo_v1_sst_osi_hist.png` (histogram, red shading for 6 cells with OSI > 1).

## Caveats / next steps
- **OSI > 1.0** (6 cells): occurs when the orthogonal response is suppressed *below* baseline (negative R_orth) — valid physiology, values saved raw.
- **2 NaN cells**: total response was zero at the preferred orientation (likely low signal-to-noise ROIs).
- **Preferred-TF approach**: OSI is computed at the single best TF per cell; an alternative is to average across all TFs before computing OSI — results would differ slightly for broadly-tuned cells.
- **AllenSDK not used**: a future run could install `allensdk` + `SimpleITK` in a different environment to cross-check using the official `DriftingGratings.get_osi()` method.
- 18 NWBs on disk lack drifting-gratings entirely (Session B / C2); the full Allen Visual Coding dataset has many more experiments available via API download if needed.

## Files

- [`code/_cell_0001.py`](./code/_cell_0001.py)
- [`code/_cell_0002.py`](./code/_cell_0002.py)
- [`code/_cell_0003.py`](./code/_cell_0003.py)
- [`code/_cell_0004.py`](./code/_cell_0004.py)
- [`code/_cell_0005.py`](./code/_cell_0005.py)
- [`code/_cell_0006.py`](./code/_cell_0006.py)
- [`code/_cell_0007.py`](./code/_cell_0007.py)
- [`code/_cell_0008.py`](./code/_cell_0008.py)
- [`code/_cell_0009.py`](./code/_cell_0009.py)
- [`code/_cell_0010.py`](./code/_cell_0010.py)
- [`code/_cell_0011.py`](./code/_cell_0011.py)
- [`code/_cell_0012.py`](./code/_cell_0012.py)
- [`code/_cell_0013.py`](./code/_cell_0013.py)
- [`code/_cell_0014.py`](./code/_cell_0014.py)
- [`code/_cell_0015.py`](./code/_cell_0015.py)
- [`code/_cell_0016.py`](./code/_cell_0016.py)
- [`code/_cell_0017.py`](./code/_cell_0017.py)
- [`code/_cell_0018.py`](./code/_cell_0018.py)
- [`code/_cell_0019.py`](./code/_cell_0019.py)
- [`code/_cell_0020.py`](./code/_cell_0020.py)
- [`code/_cell_0021.py`](./code/_cell_0021.py)
- [`code/_cell_0022.py`](./code/_cell_0022.py)
- [`code/_cell_0023.py`](./code/_cell_0023.py)
- [`code/_cell_0024.py`](./code/_cell_0024.py)
- [`code/_cell_0025.py`](./code/_cell_0025.py)
- [`figures/abo_v1_sst_osi_hist.png`](./figures/abo_v1_sst_osi_hist.png)
- [`summary.md`](./summary.md)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/abo_v1_sst_osi.csv`](./tables/abo_v1_sst_osi.csv)
- [`tables/fontlist-v390.json`](./tables/fontlist-v390.json)
