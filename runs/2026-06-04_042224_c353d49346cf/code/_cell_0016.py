# Build explicit list of SST cell columns that exist in the matrix
sst_cols_in_matrix = [c for c in all_cols if c in sst_ids]
print(f"SST cells found in matrix: {len(sst_cols_in_matrix)}")

# Load with usecols as explicit list + index_col=0 (gene names)
print("Loading count matrix for SST cells only…")
counts = pd.read_csv(
    COUNT_CSV,
    index_col=0,
    usecols=[0] + [i+1 for i, c in enumerate(all_cols) if c in sst_ids]
)
print("Shape (genes × SST cells):", counts.shape)
print("Index (gene names) sample:", counts.index[:5].tolist())
print("Columns sample:", counts.columns[:3].tolist())