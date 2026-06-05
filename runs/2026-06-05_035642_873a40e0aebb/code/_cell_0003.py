
# Check SST clusters specifically
sst = adata[adata.obs['cell_subclass'] == 'Sst']
print("SST cells:", sst.n_obs)
print("\nSST clusters:")
for c, n in sst.obs['cell_cluster'].value_counts().items():
    print(f"  {c!r}: {n}")
print("\nX dtype:", adata.X.dtype, "  min:", adata.X.min(), "  max:", adata.X.max())
