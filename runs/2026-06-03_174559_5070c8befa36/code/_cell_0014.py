
# Final validation of all three outputs
import os

for path in ['/work/sst_subtype_markers_v1_vs_alm.csv',
             '/work/sst_subtype_dotplot.png',
             '/work/sst_subtype_markers_notes.md']:
    size = os.path.getsize(path)
    print(f"  {path}: {size:,} bytes  ✓")

# Quick CSV spot-check
import pandas as pd
df = pd.read_csv('/work/sst_subtype_markers_v1_vs_alm.csv')
print(f"\nCSV shape: {df.shape} (expected 41 rows × 15 cols)")
print(df[['cell_cluster','region','n_cells','mean_log_Calb2','frac_Chrna2']].tail(5).to_string())
