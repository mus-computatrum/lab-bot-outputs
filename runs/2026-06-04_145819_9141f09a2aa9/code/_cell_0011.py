
# Check subclass column for Sst
sst_subclass = pivoted[pivoted['subclass'].str.contains('Sst', na=False)]
print("Sst subclass rows:", len(sst_subclass))
print(sst_subclass['subclass'].unique()[:10])
print(sst_subclass['class'].unique())

# Check if 'Sst' appears anywhere in the taxonomy
print("\nClasses containing GABA:")
print(sorted([c for c in pivoted['class'].unique() if 'GABA' in c]))
