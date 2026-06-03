
# Inspect key obs fields and check .X vs .layers
print("dissected_region values:", full.obs['dissected_region'].value_counts().to_dict())
print("\ncell_subclass SST values:", sorted(full.obs['cell_subclass'].dropna().unique()))
print("\nSST subclasses:")
print(full.obs['cell_subclass'].value_counts()[
    full.obs['cell_subclass'].value_counts().index.str.contains('Sst', case=False, na=False)
])

# Check .X dtype and sample values
print("\n.X dtype:", full.X.dtype)
print(".X sample (first cell, first 5 genes):", full.X[0, :5].toarray() if hasattr(full.X, 'toarray') else full.X[0, :5])

# Check .layers['counts']
print("\n.layers['counts'] dtype:", full.layers['counts'].dtype)
sample = full.layers['counts'][0, :5]
print(".layers['counts'] sample:", sample.toarray() if hasattr(sample, 'toarray') else sample)
