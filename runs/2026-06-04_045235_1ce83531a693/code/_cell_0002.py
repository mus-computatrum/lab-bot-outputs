
import pandas as pd

# Peek at the taxonomy pivot table columns first
pivot_path = "/data/yao2023-wmb-10x/_abc_cache/metadata/WMB-taxonomy/20231215/views/cluster_to_cluster_annotation_membership_pivoted.csv"
piv = pd.read_csv(pivot_path, nrows=5)
print("Taxonomy pivot columns:", piv.columns.tolist())
print(piv.head(3).to_string())
