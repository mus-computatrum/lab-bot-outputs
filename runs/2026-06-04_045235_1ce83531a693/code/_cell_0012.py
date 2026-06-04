
# Step 4: save top 10 to CSV
top10 = supertype_counts.head(10).copy()
top10["fraction_of_visp_sst"] = top10["fraction_of_visp_sst"].round(6)
out_path = "/work/yao_visp_sst_supertypes.csv"
top10.to_csv(out_path, index=False)
print("Saved:", out_path)
print(top10.to_string(index=False))
