
# These don't encode VISp. Let me look at the cluster annotation term 
# to see if VISp is referenced anywhere
print("Terms containing VIS in name:")
cluster_meta_path = "/data/yao2023-wmb-10x/_abc_cache/metadata/WMB-taxonomy/20231215/cluster_annotation_term.csv"
cat_df = pd.read_csv(cluster_meta_path)
vis_terms = cat_df[cat_df['name'].str.contains('VIS', na=False, case=False)]
print(vis_terms[['label', 'name', 'cluster_annotation_term_set_name']].head(20))
