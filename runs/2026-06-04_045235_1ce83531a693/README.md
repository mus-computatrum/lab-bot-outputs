# Run `1ce83531a693` — research

**When (UTC):** 2026-06-04 04:52:35
**Datasets:** `yao2023-wmb-10x`

## Request

> [bench:research-yao-isocortex-sst-supertypes] Using Yao 2023 WMB-10X (Isocortex subset) at /data/yao2023-wmb-10x/_abc_cache/, use abc_atlas_access to find all Sst-class cells in the VISp dissection region, rank Sst supertypes by cell count in VISp, and save the top 10 to /work/yao_visp_sst_supertypes.csv (columns: supertype, n_cells_in_visp, fraction_of_visp_sst). Use the cluster_to_cluster_annotation_membership_pivoted lookup for the supertype labels.

## Summary

All done. Here's the report:

---

## Summary
Loaded the Yao 2023 WMB-10X cell metadata (4M cells) and taxonomy pivot table, filtered for the visual cortex (`VIS`) dissection region, identified 11,932 cortical Sst interneurons spanning 17 supertypes, and saved the top 10 to `/work/yao_visp_sst_supertypes.csv`. The dominant supertype is `0217 Sst Gaba_4` (3,325 cells, ~28% of all VIS Sst cells).

## What I did
- Loaded `cell_metadata.csv` (4,042,976 cells) — just 3 columns (`cell_label`, `cluster_alias`, `region_of_interest_acronym`) to stay lean
- Loaded `cluster_to_cluster_annotation_membership_pivoted.csv` (5,322 clusters) for supertype labels
- Identified cortical Sst clusters: `07 CTX-MGE GABA` class with `053 Sst Gaba` subclass → 73 cluster aliases, 19 supertypes
- Filtered cells: `region_of_interest_acronym == "VIS"` → **11,932 Sst cells**, all subclass `053 Sst Gaba` (Sst Chodl was absent from VIS)
- Ranked 17 supertypes; saved top 10 → **`/work/yao_visp_sst_supertypes.csv`** (columns: `supertype`, `n_cells_in_visp`, `fraction_of_visp_sst`)

Top 3: `0217 Sst Gaba_4` (27.9%), `0214 Sst Gaba_1` (12.4%), `0223 Sst Gaba_10` (11.0%)

## Caveats / next steps
- **VISp granularity**: this dataset's finest dissection ROI for visual cortex is `"VIS"` (all visual areas), not `"VISp"` specifically — VISl, VISal, VISrl etc. are included. No finer spatial metadata is in the cell_metadata.csv.
- **"Sst class" interpretation**: in the WMB taxonomy, Sst sits at the *subclass* level (not class). I filtered by `07 CTX-MGE GABA` class + `053 Sst Gaba` subclass. `056 Sst Chodl Gaba` was present in taxonomy but had 0 cells in VIS.
- **Expression not loaded**: if you want marker expression per supertype, you'd need to load the `log2.h5ad` expression chunks (several GB) and join on cell_label.

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
- [`summary.md`](./summary.md)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/yao_visp_sst_supertypes.csv`](./tables/yao_visp_sst_supertypes.csv)
