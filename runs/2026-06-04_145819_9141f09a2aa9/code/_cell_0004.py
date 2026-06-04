
# VISp isn't a direct ROI — check region_of_interest_metadata
roi_meta = pd.read_csv(f"{base}/metadata/WMB-10X/20241115/region_of_interest_metadata.csv")
print("ROI metadata shape:", roi_meta.shape)
print(roi_meta.columns.tolist())
print(roi_meta.head(10))
