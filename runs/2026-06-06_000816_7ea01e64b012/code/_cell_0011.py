
# Final validation — confirm both files are readable and well-formed
import pandas as pd

df_check = pd.read_csv("/work/cave_tables.csv")
print(f"cave_tables.csv: {len(df_check)} rows × {len(df_check.columns)} cols")
print("Columns:", list(df_check.columns))
print("Voxel resolution value_counts:")
print(df_check["voxel_resolution_nm"].value_counts().to_string())

with open("/work/cave_summary.md") as f:
    lines = f.readlines()
print(f"\ncave_summary.md: {len(lines)} lines, {sum(len(l) for l in lines)} chars")
print("Section headers:", [l.strip() for l in lines if l.startswith("## ")])
