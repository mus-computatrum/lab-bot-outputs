# Run `9141f09a2aa9` — research

**When (UTC):** 2026-06-04 14:58:19
**Datasets:** `yao2023-wmb-10x`

## Request

> [bench:research-yao-isocortex-sst-supertypes] Using Yao 2023 WMB-10X (Isocortex subset) at /data/yao2023-wmb-10x/_abc_cache/, use abc_atlas_access to find all Sst-class cells in the VISp dissection region, rank Sst supertypes by cell count in VISp, and save the top 10 to /work/yao_visp_sst_supertypes.csv (columns: supertype, n_cells_in_visp, fraction_of_visp_sst). Use the cluster_to_cluster_annotation_membership_pivoted lookup for the supertype labels.

## Summary

## Summary
Found 12,279 SST interneurons in the VISp (WMB `VIS` ROI) of the Yao 2023 Whole Mouse Brain 10X atlas. These span 19 supertypes; the top 10 account for 93.8% of all SST cells and are saved to `/work/yao_visp_sst_supertypes.csv`. The dominant supertype by far is **0217 Sst Gaba_4** (3,325 cells, 27.1%).

## What I did
- Loaded the `cluster_to_cluster_annotation_membership_pivoted.csv` (taxonomy lookup) to identify all 91 Sst cluster aliases under subclasses `053 Sst Gaba` and `056 Sst Chodl Gaba` (CTX-MGE class)
- Read the VIS partition of the partitioned-parquet `cell_metadata.parquet` (321,908 cells) — the finest visual cortex dissection region available on disk (no separate 'VISp' partition exists)
- Merged cell ↔ taxonomy on `cluster_alias`, counted cells per supertype, computed fractions
- Saved top 10 to **`/work/yao_visp_sst_supertypes.csv`** with columns: `supertype`, `n_cells_in_visp`, `fraction_of_visp_sst`

| rank | supertype | n_cells | fraction |
|---|---|---|---|
| 1 | 0217 Sst Gaba_4 | 3325 | 0.271 |
| 2 | 0214 Sst Gaba_1 | 1485 | 0.121 |
| 3 | 0223 Sst Gaba_10 | 1316 | 0.107 |
| 4 | 0222 Sst Gaba_9 | 1126 | 0.092 |
| 5 | 0220 Sst Gaba_7 | 1076 | 0.088 |

## Caveats / next steps
- **"VIS" ≠ strictly VISp**: the `VIS` ROI contains primary visual cortex (VISp) plus neighboring visual areas (VISl, VISal, VISpm, etc.); no finer partition is present in the cached data. Results therefore include a small fraction of non-VISp visual cortex cells.
- `056 Sst Chodl Gaba` (long-range projecting SST) is included — only 2 of its supertypes appeared in VIS (339 + 8 cells); exclude them if you want only local Sst interneurons.
- The `cell_metadata_with_cluster_annotation` view is not cached on disk; the manual merge approach used here is the correct workaround.

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
- [`code/_cell_0026.py`](./code/_cell_0026.py)
- [`code/_cell_0027.py`](./code/_cell_0027.py)
- [`code/_cell_0028.py`](./code/_cell_0028.py)
- [`code/_cell_0029.py`](./code/_cell_0029.py)
- [`code/_cell_0030.py`](./code/_cell_0030.py)
- [`code/_cell_0031.py`](./code/_cell_0031.py)
- [`code/_cell_0032.py`](./code/_cell_0032.py)
- [`code/_cell_0033.py`](./code/_cell_0033.py)
- [`code/_cell_0034.py`](./code/_cell_0034.py)
- [`summary.md`](./summary.md)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/yao_visp_sst_supertypes.csv`](./tables/yao_visp_sst_supertypes.csv)
