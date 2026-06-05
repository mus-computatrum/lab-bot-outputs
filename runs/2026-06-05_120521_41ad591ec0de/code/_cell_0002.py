
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- counts ---
counts = (
    adata.obs["cell_cluster"]
    .value_counts()
    .reset_index()
)
counts.columns = ["cell_type", "n_cells"]
counts = counts.sort_values("n_cells", ascending=False).reset_index(drop=True)

print(f"Total cell types: {len(counts)}")
print(f"Total cells:      {counts['n_cells'].sum()}")
print(counts.head(10).to_string())

# --- save CSV ---
counts.to_csv("/work/celltype_counts.csv", index=False)
print("\nSaved /work/celltype_counts.csv")
