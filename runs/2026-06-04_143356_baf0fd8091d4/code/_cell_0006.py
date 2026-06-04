
# Quick sanity check on saved files
import os
for f in ["/work/vizgen_receptor_summary.csv", "/work/vizgen_receptor_spatial.png"]:
    sz = os.path.getsize(f)
    print(f"{f}  →  {sz/1024:.1f} KB")

# Re-read and print to confirm correctness
import pandas as pd
df = pd.read_csv("/work/vizgen_receptor_summary.csv")
print("\n", df.to_string(index=False))
