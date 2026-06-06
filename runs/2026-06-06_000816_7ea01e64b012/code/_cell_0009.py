
import pandas as pd

# Save the CSV with exactly the requested columns
df_out = df[["table_name", "voxel_resolution_nm", "table_metadata_url"]].copy()
df_out.to_csv("/work/cave_tables.csv", index=False)
print("Saved /work/cave_tables.csv —", len(df_out), "rows")
print(df_out.head(3).to_string())
