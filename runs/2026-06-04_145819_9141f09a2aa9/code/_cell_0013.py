
# Load cell_metadata_with_cluster_annotation - this has dissection_region_label
cell_ann = cache.get_metadata_dataframe(
    directory="WMB-10X",
    file_name="cell_metadata_with_cluster_annotation"
)
print("cell_ann shape:", cell_ann.shape)
print("columns:", cell_ann.columns.tolist())
