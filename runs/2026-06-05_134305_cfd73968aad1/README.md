# Run `cfd73968aad1` — research

**When (UTC):** 2026-06-05 13:43:05
**Datasets:** `tasic2018-v1`

## Request

> [bench:research-easy-tasic-celltype-counts] Count cells per cell type (use the 'cluster' field) in the Tasic 2018 V1 dataset. Produce: /work/celltype_counts.csv (two columns: cell_type, n_cells, sorted descending), and /work/celltype_counts_bar.png (horizontal bar plot of the top 30 types). Use the V1-only object pointed at by the dataset's access snippet.

## Summary

Both artifacts are saved and verified. Here's the wrap-up:

---

## Summary
Loaded the Tasic 2018 V1-only processed object (`v1_all_proc.h5ad`, 13,586 cells) and counted cells by `cell_cluster`. There are **118 distinct cell types**; the top type is *L4 IT VISp Rspo1* (1,350 cells, ~10%). The full ranked table is in the CSV and the top-30 are visualized in the bar chart, color-coded by broad class (excitatory = blue, inhibitory = orange, non-neuronal = gray).

## What I did
- Loaded `/data/tasic2018-v1/v1_all_proc.h5ad` (the dataset card's recommended V1 entry point, 13,586 × 27,505)
- Counted `cell_cluster` values, sorted descending → **`/work/celltype_counts.csv`** (118 rows × 2 columns: `cell_type`, `n_cells`)
- Generated a horizontal bar chart of the top 30 types, colored by class (excitatory/inhibitory/non-neuronal) using the Okabe-Ito colorblind-safe palette → **`/work/celltype_counts_bar.png`**
- Figure follows Tufte data-ink principles: no top/right spines, horizontal grid only, count labels at bar ends, constrained layout

## Caveats / next steps
- The V1 object has **13,586 cells across 118 types** (vs. 14,662 raw VISp cells in the full h5ad) — the processed object applies QC filters, so ~1,076 cells are excluded; this is expected
- Color assignment is rule-based (keyword matching on cluster name), so rare edge cases could be mis-colored — spot-check if using for publication
- The CSV covers all 118 types; the PNG shows only top 30 — if you need all 118 plotted, ask and I can produce a taller figure

## Files

- [`code/_cell_0001.py`](./code/_cell_0001.py)
- [`code/_cell_0002.py`](./code/_cell_0002.py)
- [`code/_cell_0003.py`](./code/_cell_0003.py)
- [`code/_cell_0004.py`](./code/_cell_0004.py)
- [`figures/celltype_counts_bar.png`](./figures/celltype_counts_bar.png)
- [`notebook.ipynb`](./notebook.ipynb)
- [`summary.md`](./summary.md)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/celltype_counts.csv`](./tables/celltype_counts.csv)
