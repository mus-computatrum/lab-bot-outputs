
df = pd.DataFrame(rows)
# Print all tables with their voxel resolution & schema
print(df[["table_name","schema","voxel_resolution_nm","http_status"]].to_string(index=False))
