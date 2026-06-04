
import pandas as pd
import os

# Load cell metadata - filter to VIS region of interest
meta_path = "/data/yao2023-wmb-10x/_abc_cache/metadata/WMB-10X/20241115/cell_metadata.parquet"
taxonomy_path = "/data/yao2023-wmb-10x/_abc_cache/metadata/WMB-taxonomy/20231215/views/cluster_to_cluster_annotation_membership_pivoted.csv"

print("Loading taxonomy pivot table...")
taxonomy = pd.read_csv(taxonomy_path)
print(f"Taxonomy shape: {taxonomy.shape}")
print(f"Taxonomy columns: {taxonomy.columns.tolist()[:10]}")
print(taxonomy.head(2))
