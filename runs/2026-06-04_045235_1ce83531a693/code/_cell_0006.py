
# Check Sst class in taxonomy pivot
piv = pd.read_csv(pivot_path)
print(f"Taxonomy pivot shape: {piv.shape}")
# Find Sst class
sst_classes = piv[piv["class"].str.contains("Sst", na=False)]["class"].unique()
print("SST-related classes:", sst_classes)

# Also check subclass for Sst
sst_subclasses = piv[piv["subclass"].str.contains("Sst", na=False)]["subclass"].unique()
print("\nSST-related subclasses (sample):", sst_subclasses[:10])
