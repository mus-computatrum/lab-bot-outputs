
# ── 8. Validate outputs ───────────────────────────────────────────────────────
import os
csv_size = os.path.getsize('/work/chrm_mouse_marmoset.csv')
png_size = os.path.getsize('/work/chrm_dotplot.png')
print(f"CSV: {csv_size} bytes")
print(f"PNG: {png_size/1024:.1f} KB")

# Quick sanity check on CSV contents
df_check = pd.read_csv('/work/chrm_mouse_marmoset.csv')
print(f"\nCSV shape: {df_check.shape}")
print(df_check.to_string(index=False))
