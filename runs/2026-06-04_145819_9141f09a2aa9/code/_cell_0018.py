
# The cell_metadata.csv is large (1 GB) - already loaded. Let's look at what ROI breakdown we have
# Check the cluster_annotation_term for dissection region info
print("Cluster annotation term set names:")
term_set = pd.read_csv(f"{base}/../WMB-taxonomy/20231215/cluster_annotation_term_set.csv" \
    .replace('WMB-10X/20241115', 'WMB-taxonomy/20231215'))

# Actually use absolute path
term_set = pd.read_csv("/data/yao2023-wmb-10x/_abc_cache/metadata/WMB-taxonomy/20231215/cluster_annotation_term_set.csv")
print(term_set)
