# Run `c22aeee6cf41` — research

**When (UTC):** 2026-06-05 12:02:05
**Datasets:** `tasic2018-v1`

## Request

> [bench:research-easy-tasic-celltype-counts] Count cells per cell type (use the 'cluster' field) in the Tasic 2018 V1 dataset. Produce: /work/celltype_counts.csv (two columns: cell_type, n_cells, sorted descending), and /work/celltype_counts_bar.png (horizontal bar plot of the top 30 types). Use the V1-only object pointed at by the dataset's access snippet.

## Summary

All 13,586 cells are confirmed VISp. The 4 bottom-of-list types with "ALM" in the name are VISp cells assigned to ALM-named clusters in the shared taxonomy — that's a known feature of Tasic 2018 (a handful of VISp cells map to cross-area clusters). Both artifacts are clean.

---

## Summary
Counted all cells in the Tasic 2018 VISp-only object (`v1_all_proc.h5ad`) by the `cell_cluster` field: **13,586 cells across 118 transcriptomic clusters**. The largest type is **L4 IT VISp Rspo1** (1,350 cells, ~10% of the dataset); the top 30 clusters together account for ~10,500 cells. Four clusters have only 1 cell and carry "ALM" labels — VISp cells assigned to cross-area clusters in the shared taxonomy, a known quirk of this dataset.

## What I did
- Loaded `/data/tasic2018-v1/v1_all_proc.h5ad` (13,586 VISp cells × 27,505 genes)
- Counted `cell_cluster` with `.value_counts()`, sorted descending
- Saved **`/work/celltype_counts.csv`** — 118 rows, columns `cell_type`, `n_cells`
- Saved **`/work/celltype_counts_bar.png`** — horizontal bar chart of top 30 types, color-coded by class (blue=excitatory, red=inhibitory, green=non-neuronal)

## Caveats / next steps
- 4 rare (n=1) clusters have "ALM" in their name despite being in the V1 object — these are correctly present (shared cross-area clusters in the Tasic 2018 taxonomy); filter by name if you want pure "VISp-named" clusters only.
- Color coding is name-based heuristic; a handful of types (e.g. `CR`, `Meis2`) may be mis-colored — check against the `cell_class` column for precision.
- This uses `cell_cluster`; for coarser resolution use `cell_subclass` or `cell_class`.

## Files

- [`code/_cell_0001.py`](./code/_cell_0001.py)
- [`code/_cell_0002.py`](./code/_cell_0002.py)
- [`code/_cell_0003.py`](./code/_cell_0003.py)
- [`code/_cell_0004.py`](./code/_cell_0004.py)
- [`code/_cell_0005.py`](./code/_cell_0005.py)
- [`figures/celltype_counts_bar.png`](./figures/celltype_counts_bar.png)
- [`notebook.ipynb`](./notebook.ipynb)
- [`summary.md`](./summary.md)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/celltype_counts.csv`](./tables/celltype_counts.csv)
- [`tables/fontlist-v390.json`](./tables/fontlist-v390.json)
