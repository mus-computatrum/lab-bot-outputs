
# Find Sst class entries
sst_classes = pivoted[pivoted['class'].str.contains('Sst', na=False)]
print("Sst class unique values:", pivoted['class'].str.contains('Sst', na=False).sum())
print(pivoted['class'].unique()[:20])
