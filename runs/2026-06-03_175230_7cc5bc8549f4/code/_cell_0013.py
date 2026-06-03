
# Check cell-type labels, clusters, and counts matrix
import pandas as pd

print("=== uns metadata ===")
for k in adata.uns.keys():
    v = adata.uns[k]
    print(f"  {k}: {str(v)[:200]}")

print("\n=== First 10 unique cell_type labels ===")
ct = adata.obs['cell_type']
unique_ct = ct.unique()
print(f"Total cell types: {len(unique_ct)}")
for t in sorted(unique_ct)[:10]:
    count = (ct == t).sum()
    print(f"  {t}: {count:,} cells")

print("\n=== First 10 unique Cluster labels ===")
cl = adata.obs['Cluster']
unique_cl = cl.unique()
print(f"Total clusters: {len(unique_cl)}")
for c in sorted(unique_cl)[:10]:
    count = (cl == c).sum()
    print(f"  {c}: {count:,} cells")

print("\n=== First 10 unique Subclass labels ===")
sc = adata.obs['Subclass']
unique_sc = sc.unique()
print(f"Total subclasses: {len(unique_sc)}")
for s in sorted(unique_sc)[:10]:
    count = (sc == s).sum()
    print(f"  {s}: {count:,} cells")
