
# The pivoted file is in views/ - let's reload it directly to make sure we have the right one
pivoted_path = views_path + "/cluster_to_cluster_annotation_membership_pivoted.csv"
pivoted = pd.read_csv(pivoted_path)
print("Pivoted shape:", pivoted.shape)
print("Columns:", pivoted.columns.tolist())
print(pivoted[pivoted['subclass'].str.contains('Sst', na=False)].head(5))
