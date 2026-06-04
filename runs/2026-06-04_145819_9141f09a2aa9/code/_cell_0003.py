
# Check region_of_interest_acronym values for VISp
print("Unique ROI values (sample):", cell_meta['region_of_interest_acronym'].unique()[:30])
print("\nVISp count:", (cell_meta['region_of_interest_acronym'] == 'VISp').sum())

# Load cluster annotation term CSV to understand taxonomy
cluster_ann = pd.read_csv(f"{base}/metadata/WMB-taxonomy/20231215/cluster_annotation_term.csv")
print("\ncluster_annotation_term shape:", cluster_ann.shape)
print("columns:", cluster_ann.columns.tolist())
print(cluster_ann.head(3))
