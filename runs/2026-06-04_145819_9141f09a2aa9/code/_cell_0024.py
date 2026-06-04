
# Read the VIS partition (this dataset uses 'VIS' for what includes VISp)
vis_part = pd.read_parquet(os.path.join(pq_dir, "region_of_interest_acronym=VIS"))
print("VIS partition shape:", vis_part.shape)
print("Columns:", vis_part.columns.tolist())
print(vis_part.head(3))
