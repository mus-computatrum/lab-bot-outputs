
import os
csv_size = os.path.getsize("/work/celltype_counts.csv")
png_size = os.path.getsize("/work/celltype_counts_bar.png")
print(f"celltype_counts.csv : {csv_size:,} bytes")
print(f"celltype_counts_bar.png: {png_size:,} bytes")

# Verify CSV
df = pd.read_csv("/work/celltype_counts.csv")
print(f"\nCSV rows: {len(df)}  |  cols: {list(df.columns)}")
print(f"Top: {df.iloc[0]['cell_type']} ({df.iloc[0]['n_cells']} cells)")
print(f"Bottom: {df.iloc[-1]['cell_type']} ({df.iloc[-1]['n_cells']} cells)")
print(f"Sum: {df['n_cells'].sum()} (expected 13,586)")
print(f"Sorted descending: {(df['n_cells'].diff().dropna() <= 0).all()}")
