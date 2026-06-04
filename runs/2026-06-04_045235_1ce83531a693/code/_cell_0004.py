
# Load only needed columns from cell metadata (it's ~1 GB, so load selectively)
print("Loading cell metadata (subset of columns)...")
cells = pd.read_csv(cell_path, usecols=["cell_label", "cluster_alias", "region_of_interest_acronym"])
print(f"Loaded: {cells.shape}")
print("Region of interest unique values (sample):", cells["region_of_interest_acronym"].value_counts().head(20))
