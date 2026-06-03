
# Investigate marmoset normalization state - max of 125 is suspicious for log1p
print("Marmoset X dtype:", adata_mar.X.dtype)
print("Marmoset X type:", type(adata_mar.X))

# Sample a few values
if sp.issparse(adata_mar.X):
    sample = adata_mar.X[:100,:].toarray()
else:
    sample = np.array(adata_mar.X[:100,:])

print(f"First 100 cells, all genes: min={sample.min():.3f}, max={sample.max():.3f}, mean={sample.mean():.4f}")
print(f"Global max: {adata_mar.X.max():.2f}")
print(f"Non-integer fraction: {(sample % 1 != 0).mean():.3f}")
print(f"Are values integer-valued? {np.all(sample % 1 == 0)}")

# Check if there's a raw slot
print("\nRaw slot:", adata_mar.raw)
print("Layers:", list(adata_mar.layers.keys()) if adata_mar.layers else "None")
print("uns keys:", list(adata_mar.uns.keys())[:10])
