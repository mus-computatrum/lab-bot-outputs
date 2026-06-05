# Quick sanity check on outputs
import os
csv_size = os.path.getsize("/work/celltype_counts.csv")
png_size = os.path.getsize("/work/celltype_counts_bar.png")
print(f"celltype_counts.csv   : {csv_size:,} bytes ({len(counts)} rows)")
print(f"celltype_counts_bar.png: {png_size:,} bytes")

# Verify CSV structure
df_check = pd.read_csv("/work/celltype_counts.csv")
print(f"\nCSV columns: {list(df_check.columns)}")
print(f"First 5 rows:\n{df_check.head()}")
print(f"Last 5 rows:\n{df_check.tail()}")
print(f"\nMin n_cells: {df_check['n_cells'].min()}, Max: {df_check['n_cells'].max()}")
print(f"Sum: {df_check['n_cells'].sum()}")
