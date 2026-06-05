
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# ── 1. Count cells per cluster (all types, not just top-30) ──────────────────
counts = (
    adata_v1.obs["cell_cluster"]
    .value_counts()
    .rename_axis("cell_type")
    .reset_index(name="n_cells")
    .sort_values("n_cells", ascending=False)
    .reset_index(drop=True)
)
print(f"Total clusters: {len(counts)}, total cells: {counts['n_cells'].sum()}")
print(counts.head(10).to_string(index=False))

# ── 2. Save full CSV ─────────────────────────────────────────────────────────
counts.to_csv("/work/celltype_counts.csv", index=False)
print("\nSaved /work/celltype_counts.csv")
