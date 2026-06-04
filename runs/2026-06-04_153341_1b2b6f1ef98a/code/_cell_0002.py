
# Identify Sst subclasses in taxonomy
sst_tax = taxonomy[taxonomy['subclass'].str.contains('Sst', na=False)]
print("Sst subclasses found:")
print(sst_tax['subclass'].unique())
print(f"\nTotal Sst clusters: {len(sst_tax)}")
print(f"Sst cluster_aliases: {sorted(sst_tax['cluster_alias'].tolist())[:10]}...")
