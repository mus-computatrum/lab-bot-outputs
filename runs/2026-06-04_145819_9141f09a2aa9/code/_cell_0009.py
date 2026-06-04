
# Load the pivoted membership table (has supertype labels for each cluster)
pivoted = cache.get_metadata_dataframe(
    directory="WMB-taxonomy",
    file_name="cluster_to_cluster_annotation_membership_pivoted"
)
print("Pivoted shape:", pivoted.shape)
print("Columns:", pivoted.columns.tolist())
print(pivoted.head(3))
