# research-easy-tasic-celltype-counts

**Mode**: research  ·  **Effort**: standard

## Request

> Count cells per cell type (use the 'cluster' field) in the Tasic 2018 V1 dataset. Produce: /work/celltype_counts.csv (two columns: cell_type, n_cells, sorted descending), and /work/celltype_counts_bar.png (horizontal bar plot of the top 30 types). Use the V1-only object pointed at by the dataset's access snippet.

## Final summary

All outputs verified. Here's the final report:

---

## Summary
Loaded the Tasic 2018 VISp-only processed object (`v1_all_proc.h5ad`, 13,586 cells) and counted cells across all 118 `cell_cluster` types. The dominant type is **L4 IT VISp Rspo1** (1,350 cells, ~10%), followed by **L6 IT VISp Penk Col27a1** (1,031) and **L2/3 IT VISp Agmat** (658). The long tail includes 5 types with only 1 cell each (mostly ALM contamination).

## What I did
- Loaded `/data/tasic2018-v1/v1_all_proc.h5ad` (13,586 VISp cells × 27,505 genes)
- Counted cells per `cell_cluster`, sorted descending — 118 unique types, all 13,586 cells accounted for
- Saved **`/work/celltype_counts.csv`** — 118 rows, two columns (`cell_type`, `n_cells`), monotonically sorted ✓
- Saved **`/work/celltype_counts_bar.png`** — horizontal bar chart of top 30 types (154 KB), colour-coded by broad class (blue = excitatory/projection, orange = inhibitory interneuron, green = non-neuronal)

## Caveats / next steps
- The V1 object retains a handful of cells labelled as ALM types (e.g. `L6 IT ALM Tgfb1`, n=1) — these appear to be edge-case assignments in the taxonomy, not a loading error; filter on `dissected_region == 'VISp'` if strict region purity is needed.
- Colour coding in the bar plot is heuristic (string-match based), not from a curated class field — a few ambiguous names may be mis-coloured; use `cell_class` obs column for authoritative class labels.
- The plot shows the top 30 of 118 types; the full table is in the CSV.
