# Run `4646c920eb94` — research

**When (UTC):** 2026-06-03 17:41:04
**Datasets:** `tasic2018-v1`

## Request

> [bench:research-easy-tasic-celltype-counts] Count cells per cell type (use the 'cluster' field) in the Tasic 2018 V1 dataset. Produce: /work/celltype_counts.csv (two columns: cell_type, n_cells, sorted descending), and /work/celltype_counts_bar.png (horizontal bar plot of the top 30 types). Use the V1-only object pointed at by the dataset's access snippet.

## Summary

All outputs validated. Here's the summary:

---

## Summary
Loaded the Tasic 2018 V1-only object (`v1_all_proc.h5ad`, 13,586 VISp cells) and counted cells across all 118 `cell_cluster` labels. The largest cluster is **L4 IT VISp Rspo1** (1,350 cells); the smallest are singleton rare types. Both deliverables are saved to `/work`.

## What I did
- Loaded `/data/tasic2018-v1/v1_all_proc.h5ad` (13,586 cells × 27,505 genes, VISp-only confirmed via `dissected_region`)
- Counted cells per `cell_cluster`, sorted descending → **`/work/celltype_counts.csv`** (118 rows, columns: `cell_type`, `n_cells`)
- Produced **`/work/celltype_counts_bar.png`**: horizontal bar chart of the top 30 clusters, color-coded by cell class (red = GABAergic, blue = Glutamatergic, green = Non-neuronal)

## Caveats / next steps
- A handful of clusters carry **"ALM" in their name** (e.g., `L5 IT ALM Npw`, 1 cell) — this is the taxonomy cluster label from the full Tasic 2018 atlas, **not** the dissection region. All 13,586 cells confirmed as `dissected_region == VISp`.
- The cluster field used is `cell_cluster` (finest-grain level); coarser groupings like `cell_subclass` or `cell_class` are also available in `.obs` if a rolled-up count is needed.
- Counts reflect the QC-passed V1 subset (13,586 of 23,822 total cells in the full taxonomy).

## Files

- [`code/_cell_0001.py`](./code/_cell_0001.py)
- [`code/_cell_0002.py`](./code/_cell_0002.py)
- [`code/_cell_0003.py`](./code/_cell_0003.py)
- [`code/_cell_0004.py`](./code/_cell_0004.py)
- [`code/_cell_0005.py`](./code/_cell_0005.py)
- [`code/_cell_0006.py`](./code/_cell_0006.py)
- [`figures/celltype_counts_bar.png`](./figures/celltype_counts_bar.png)
- [`summary.md`](./summary.md)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/celltype_counts.csv`](./tables/celltype_counts.csv)
