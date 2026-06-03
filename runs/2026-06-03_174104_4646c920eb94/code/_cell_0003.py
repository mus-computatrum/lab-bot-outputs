import os
os.environ["MPLCONFIGDIR"] = "/work/mpl_cache"
os.makedirs("/work/mpl_cache", exist_ok=True)

# Count cells per cell_cluster, sorted descending
counts = (
    adata.obs["cell_cluster"]
    .value_counts()
    .reset_index()
)
counts.columns = ["cell_type", "n_cells"]
counts = counts.sort_values("n_cells", ascending=False).reset_index(drop=True)

print(f"Total cells: {counts['n_cells'].sum()}")
print(f"Total cell types: {len(counts)}")
print(counts.head(10))

# Save CSV
counts.to_csv("/work/celltype_counts.csv", index=False)
print("\nSaved /work/celltype_counts.csv")
