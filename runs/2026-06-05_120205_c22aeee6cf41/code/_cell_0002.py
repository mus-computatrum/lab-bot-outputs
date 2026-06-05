
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- Count cells per cluster ---
counts = (
    adata.obs["cell_cluster"]
    .value_counts()
    .reset_index()
)
counts.columns = ["cell_type", "n_cells"]
counts = counts.sort_values("n_cells", ascending=False).reset_index(drop=True)

print(f"Total cells: {counts['n_cells'].sum()}")
print(f"Unique clusters: {len(counts)}")
print(counts.head(10).to_string(index=False))

# --- Save CSV ---
counts.to_csv("/work/celltype_counts.csv", index=False)
print("\nSaved /work/celltype_counts.csv")
