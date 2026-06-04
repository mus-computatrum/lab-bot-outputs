# Run `baf0fd8091d4` — research

**When (UTC):** 2026-06-04 14:33:56
**Datasets:** `vizgen-merfish-brain-map`

## Request

> [bench:research-vizgen-spatial-marker-genes] Using Vizgen MERFISH Slice 3 Replicate 1 at /data/vizgen-merfish-brain-map/Slice3_Replicate1/, load the detected_transcripts (prefer the parquet at detected_transcripts.parquet/ if present; otherwise fall back to detected_transcripts.csv) and for each of the four panel receptor genes Sstr1, Sstr2, Crhr1, Oprk1 (all confirmed in the panel — DO NOT spend turns checking): (a) count detected transcripts, (b) compute the mean global_x + global_y of their detections, (c) compute the spatial spread (std of global_x + global_y). Save /work/vizgen_receptor_summary.csv (columns: gene, n_transcripts, mean_x, mean_y, std_x, std_y) and one scatter plot at /work/vizgen_receptor_spatial.png (distribution of each receptor with a different color). Be efficient — if the parquet directory exists, use pyarrow.parquet.read_table(...) with a gene-filter so you only touch the relevant partitions; do NOT scan the whole file.

## Summary

Both artifacts are clean. Here's the wrap-up:

---

## Summary
Loaded 298,095 transcript detections across four receptor genes (Sstr1, Sstr2, Crhr1, Oprk1) from the Vizgen MERFISH Slice 3 Replicate 1 parquet dataset using per-gene partition reads — no full-file scan needed. **Oprk1** is the most abundant (~86 K transcripts) and is spatially shifted toward higher x/y coordinates relative to the other three, which cluster more centrally. Sstr1 is the least abundant (~53 K) and has intermediate spread.

## What I did
- Confirmed `detected_transcripts.parquet/` exists with Hive partitioning (`gene=<name>/`); read **only the 4 target partitions** via `pyarrow.parquet.read_table()` — no CSV scan.
- Computed per-gene: `n_transcripts`, `mean_x`, `mean_y`, `std_x`, `std_y`.
- Saved **`/work/vizgen_receptor_summary.csv`** (4 rows × 6 cols):

| gene | n_transcripts | mean_x | mean_y | std_x | std_y |
|------|---:|---:|---:|---:|---:|
| Sstr1 | 52,628 | 3409.55 | 3899.57 | 1722.23 | 1984.57 |
| Sstr2 | 80,973 | 3717.03 | 4122.44 | 1666.93 | 1929.41 |
| Crhr1 | 78,231 | 3472.39 | 3943.94 | 1820.52 | 2103.72 |
| Oprk1 | 86,263 | 4339.41 | 4759.16 | 1431.28 | 1704.84 |

- Saved **`/work/vizgen_receptor_spatial.png`** — scatter of 15 K subsampled points per gene (4 colours) with centroids marked as stars (~838 KB).

## Caveats / next steps
- Scatter uses a random subsample of 15 K per gene for visual clarity; all 298 K points were used for statistics.
- Coordinates are in raw MERFISH µm space (no CCF registration); spatial shift of Oprk1 likely reflects enrichment in a distinct anatomical compartment (e.g., lateral cortex or striatum).
- No cell-level assignment done — these are raw transcript counts, not per-cell expression. For cell-type context, join against `cell_by_gene.csv` and the Leiden clusters from the prior MERFISH job.

## Files

- [`code/_cell_0001.py`](./code/_cell_0001.py)
- [`code/_cell_0002.py`](./code/_cell_0002.py)
- [`code/_cell_0003.py`](./code/_cell_0003.py)
- [`code/_cell_0004.py`](./code/_cell_0004.py)
- [`code/_cell_0005.py`](./code/_cell_0005.py)
- [`code/_cell_0006.py`](./code/_cell_0006.py)
- [`figures/vizgen_receptor_spatial.png`](./figures/vizgen_receptor_spatial.png)
- [`summary.md`](./summary.md)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/vizgen_receptor_summary.csv`](./tables/vizgen_receptor_summary.csv)
