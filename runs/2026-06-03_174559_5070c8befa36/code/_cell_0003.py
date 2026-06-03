
# Filter to SST interneurons
sst = full[full.obs['cell_subclass'] == 'Sst'].copy()
print(f"SST cells: {sst.n_obs}")
print("\nRegion breakdown:")
print(sst.obs['dissected_region'].value_counts())
print("\nSST clusters (first 20):")
print(sst.obs['cell_cluster'].value_counts().head(20))

# Check the six marker genes are present
markers = ['Calb2', 'Crh', 'Hpse', 'Nos1', 'Pdyn', 'Chrna2']
gene_names = sst.var_names.tolist()
for m in markers:
    present = m in gene_names
    print(f"  {m}: {'FOUND' if present else 'MISSING'}")
