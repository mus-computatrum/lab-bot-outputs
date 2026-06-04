
# Save top 10 to CSV
top10 = supertype_counts.head(10).copy()
top10['fraction_of_visp_sst'] = top10['fraction_of_visp_sst'].round(6)

out_path = "/work/yao_visp_sst_supertypes.csv"
top10.to_csv(out_path, index=False)
print(f"Saved to {out_path}")
print("\nTop 10 Sst supertypes in VISp (VIS ROI):")
print(top10.to_string(index=False))

# Verify the file
print(f"\nFile size: {os.path.getsize(out_path)} bytes")
print("\nVerification read-back:")
print(pd.read_csv(out_path))
