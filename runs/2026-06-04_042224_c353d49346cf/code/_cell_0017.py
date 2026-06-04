import numpy as np

# Align cells between count matrix and metadata
common_cells = [c for c in counts.columns if c in id2ttype]
counts_sst = counts[common_cells]
print(f"Cells with both count data and metadata: {len(common_cells)}")

# Genes × cells → cells × genes for easier groupby later
# Keep as numpy (genes × cells) for per-ttype slicing
gene_names = counts_sst.index.tolist()
log1p_mat = np.log1p(counts_sst.values.astype(np.float32))   # genes × cells
print("log1p matrix shape:", log1p_mat.shape)

cell_ttypes_arr = np.array([id2ttype[c] for c in common_cells])
unique_ttypes = sorted(set(cell_ttypes_arr))
print("Unique t-types:", len(unique_ttypes))