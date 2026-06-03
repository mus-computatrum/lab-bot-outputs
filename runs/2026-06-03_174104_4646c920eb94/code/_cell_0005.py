# Quick sanity check on outputs
import os
csv_size = os.path.getsize("/work/celltype_counts.csv")
png_size = os.path.getsize("/work/celltype_counts_bar.png")
print(f"celltype_counts.csv  → {csv_size:,} bytes, {len(counts)} rows")
print(f"celltype_counts_bar.png → {png_size:,} bytes")

# Preview top & bottom of CSV
print("\n--- Top 5 ---")
print(counts.head(5).to_string(index=False))
print("\n--- Bottom 5 ---")
print(counts.tail(5).to_string(index=False))
