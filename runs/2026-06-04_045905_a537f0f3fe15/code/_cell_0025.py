# Verify outputs exist
import os
for f in ['/work/abo_v1_sst_osi.csv', '/work/abo_v1_sst_osi_hist.png']:
    sz = os.path.getsize(f)
    print(f"{f}  ({sz/1e3:.1f} KB)")

# Spot-check CSV
df_check = pd.read_csv('/work/abo_v1_sst_osi.csv')
print(f"\nCSV shape: {df_check.shape}, columns: {list(df_check.columns)}")
print(df_check.describe())
