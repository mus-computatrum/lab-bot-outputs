
# --- Cell-type counts ---
counts = (
    adata.obs["cell_cluster"]
    .value_counts()                      # sorted descending by default
    .reset_index()
)
counts.columns = ["cell_type", "n_cells"]
print(f"Total cells: {counts['n_cells'].sum()}  |  Unique types: {len(counts)}")
print(counts.head(10).to_string(index=False))

# Save CSV
counts.to_csv("/work/celltype_counts.csv", index=False)
print("\nSaved /work/celltype_counts.csv")
