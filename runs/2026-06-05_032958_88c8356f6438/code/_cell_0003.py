import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# --- Count cells per cluster, sorted descending ---
counts = (
    adata.obs["cell_cluster"]
    .value_counts()
    .reset_index()
)
counts.columns = ["cell_type", "n_cells"]
counts = counts.sort_values("n_cells", ascending=False).reset_index(drop=True)

print(f"Total cells: {counts['n_cells'].sum()}")
print(f"Unique clusters: {len(counts)}")
print(counts.head(10))

# Save CSV
counts.to_csv("/work/celltype_counts.csv", index=False)
print("\nSaved /work/celltype_counts.csv")
