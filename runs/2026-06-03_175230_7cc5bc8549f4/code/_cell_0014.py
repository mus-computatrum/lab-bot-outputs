
# Check counts matrix and gene names
import scipy.sparse as sp

print("=== Counts Matrix (X) ===")
X = adata.X
print(f"  dtype: {X.dtype}")
print(f"  type: {type(X)}")
print(f"  shape: {X.shape}")

# Load a small slice to check values
X_slice = adata.X[:5, :5]
if sp.issparse(X_slice):
    X_slice = X_slice.toarray()
print(f"  first 5x5 values:\n{X_slice}")

print("\n=== Gene names (first 10) ===")
print(adata.var['feature_name'][:10].tolist())

print("\n=== Sample obs (first 2 rows) ===")
print(adata.obs[['Cluster', 'Subclass', 'cell_type', 'donor_id', 'tissue']].head(2).to_string())

print("\n=== All unique tissues ===")
print(adata.obs['tissue'].unique().tolist())

print("\n=== Subclasses full list ===")
sc_counts = adata.obs['Subclass'].value_counts()
for sc_name, count in sc_counts.items():
    print(f"  {sc_name}: {count:,}")

print("\n=== CrossSpeciesCluster (first 10 unique) ===")
csc = adata.obs['CrossSpeciesCluster'].unique()
print(f"Total CrossSpeciesClusters: {len(csc)}")
for c in sorted(csc)[:10]:
    print(f"  {c}")
