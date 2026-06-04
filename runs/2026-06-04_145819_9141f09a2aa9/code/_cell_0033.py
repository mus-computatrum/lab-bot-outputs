
# Save top 10 to /work
top10 = supertype_counts.head(10).copy()
out_path = "/work/yao_visp_sst_supertypes.csv"
top10.to_csv(out_path, index=False)
print("Saved:", out_path)
print("\nTop 10 SST supertypes in VISp (WMB 'VIS' ROI):")
print(top10.to_string(index=False))
print(f"\nTop 10 cover {top10['fraction_of_visp_sst'].sum():.3f} ({top10['fraction_of_visp_sst'].sum()*100:.1f}%) of all SST cells in VIS region")
