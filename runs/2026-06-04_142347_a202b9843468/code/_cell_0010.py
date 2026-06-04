
# Final: show the saved CSV
print("=== /work/vizgen_sst_marker_summary.csv ===")
import pandas as pd
df = pd.read_csv("/work/vizgen_sst_marker_summary.csv")
print(df.to_string(index=False))

print("\n=== Proxy-gene spatial stats (for reference) ===")
print(proxy_df.to_string(index=False))

print("\nFiles saved:")
import os
for f in ["vizgen_sst_marker_summary.csv", "vizgen_sst_marker_spatial.png"]:
    path = f"/work/{f}"
    print(f"  {path}  ({os.path.getsize(path)/1e3:.1f} KB)")
