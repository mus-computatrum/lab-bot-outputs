
# Load cell metadata - only the columns we need, filtered to VIS region
print("Loading cell metadata parquet (VIS region only)...")
meta = pd.read_parquet(
    meta_path,
    columns=['cell_label', 'region_of_interest_acronym', 'cluster_alias']
)
print(f"Total cells loaded: {len(meta):,}")
print(f"Unique ROIs: {meta['region_of_interest_acronym'].nunique()}")
print(meta['region_of_interest_acronym'].value_counts().head(10))
