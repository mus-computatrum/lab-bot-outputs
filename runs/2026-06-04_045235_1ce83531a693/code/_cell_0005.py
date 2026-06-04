
# Check all VIS-related regions
vis_regions = cells["region_of_interest_acronym"].dropna().unique()
visp_related = [r for r in vis_regions if "VIS" in str(r).upper()]
print("VIS-related regions:", sorted(visp_related))

# Also check the region_of_interest_metadata for VISp
roi_path = "/data/yao2023-wmb-10x/_abc_cache/metadata/WMB-10X/20241115/region_of_interest_metadata.csv"
roi_meta = pd.read_csv(roi_path)
print("\nROI metadata columns:", roi_meta.columns.tolist())
print(roi_meta[roi_meta["acronym"].str.contains("VIS", na=False)].to_string())
