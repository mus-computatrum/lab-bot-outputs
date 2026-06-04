# Run `1b2b6f1ef98a` — research

**When (UTC):** 2026-06-04 15:33:41
**Datasets:** `yao2023-wmb-10x`

## Request

> [bench:research-yao-isocortex-sst-supertypes] Using Yao 2023 WMB-10X (Isocortex subset) at /data/yao2023-wmb-10x/_abc_cache/, use abc_atlas_access to find all Sst-class cells in the VISp dissection region, rank Sst supertypes by cell count in VISp, and save the top 10 to /work/yao_visp_sst_supertypes.csv (columns: supertype, n_cells_in_visp, fraction_of_visp_sst). Use the cluster_to_cluster_annotation_membership_pivoted lookup for the supertype labels.

## Summary

All done. The results are clean and verified. Here's the full report:

---

## Summary
Found **12,279 Sst-class cells** in the VISp dissection region (`region_of_interest_acronym='VIS'`) of the Yao 2023 Whole Mouse Brain 10X atlas, spanning **19 supertypes**. The top 10 supertypes account for **93.7%** of all VISp Sst cells and are saved to `/work/yao_visp_sst_supertypes.csv`. Supertype `0217 Sst Gaba_4` dominates at 27.1% (n=3,325).

## What I did
- Loaded `cluster_to_cluster_annotation_membership_pivoted.csv` and extracted cortical Sst subclasses (`053 Sst Gaba` + `056 Sst Chodl Gaba`; 91 clusters across 25 supertypes)
- Loaded cell metadata parquet (4M cells) and filtered to `region_of_interest_acronym == 'VIS'` → 321,908 cells → 12,279 Sst cells across 19 supertypes
- Ranked supertypes by cell count, computed fraction of VISp Sst total
- Saved **top 10** to `/work/yao_visp_sst_supertypes.csv` (columns: `supertype`, `n_cells_in_visp`, `fraction_of_visp_sst`)

| Rank | Supertype | n | Fraction |
|------|-----------|---|---------|
| 1 | 0217 Sst Gaba_4 | 3,325 | 27.1% |
| 2 | 0214 Sst Gaba_1 | 1,485 | 12.1% |
| 3 | 0223 Sst Gaba_10 | 1,316 | 10.7% |
| 4 | 0222 Sst Gaba_9 | 1,126 | 9.2% |
| 5 | 0220 Sst Gaba_7 | 1,076 | 8.8% |

## Caveats / next steps
- **VIS ≠ VISp strictly**: the `VIS` ROI includes all visual cortex sub-areas, not purely VISp primary. No finer-grained partition exists in the parquet on disk.
- **PB Sst excluded**: `265 PB Sst Gly-Gaba` (pontine brainstem) was intentionally excluded as non-cortical; only 6 supertypes more in the full 25-supertype set are not in the top 19 seen in VIS.
- The top 10 cover only `Sst Gaba` supertypes; `Sst Chodl` (#11: `0241 Sst Chodl Gaba_4`, n=339) is the first Chodl type just outside the top 10.

## Files

- [`code/_cell_0001.py`](./code/_cell_0001.py)
- [`code/_cell_0002.py`](./code/_cell_0002.py)
- [`code/_cell_0003.py`](./code/_cell_0003.py)
- [`code/_cell_0004.py`](./code/_cell_0004.py)
- [`code/_cell_0005.py`](./code/_cell_0005.py)
- [`code/_cell_0006.py`](./code/_cell_0006.py)
- [`code/_cell_0007.py`](./code/_cell_0007.py)
- [`summary.md`](./summary.md)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/yao_visp_sst_supertypes.csv`](./tables/yao_visp_sst_supertypes.csv)
