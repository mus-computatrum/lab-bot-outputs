
# Let me check what VIS-PTLp partition looks like too, and look at the ABC Atlas 
# tutorial pattern for accessing region information in WMB datasets.
# First, let's see what abc_atlas_access's get_metadata_dataframe returns for cluster
cluster_meta = cache.get_metadata_dataframe(
    directory="WMB-taxonomy",
    file_name="cluster_annotation_term"
)
print("cluster_annotation_term shape:", cluster_meta.shape)
print(cluster_meta.columns.tolist())
# Look for any dissection region terms
print("\nAll term_set names:")
print(cluster_meta['cluster_annotation_term_set_name'].unique())
