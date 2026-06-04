import pandas as pd

# Write empty CSV with correct headers (as placeholder)
df_empty = pd.DataFrame(columns=["unit_id", "pt_root_id",
                                  "pt_position_x", "pt_position_y", "pt_position_z"])
df_empty.to_csv("/work/microns_coreg_sample.csv", index=False)
print("Wrote /work/microns_coreg_sample.csv (empty — headers only)")

# Verify all outputs
import os
for f in ["/work/notes.md", "/work/run_coreg.py", "/work/microns_coreg_sample.csv"]:
    size = os.path.getsize(f)
    print(f"  {f}  ({size:,} bytes)")
