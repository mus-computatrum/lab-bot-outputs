
import os

# verify CSV
csv_df = pd.read_csv("/work/celltype_counts.csv")
print("CSV shape:", csv_df.shape)
print("Sorted descending?", csv_df["n_cells"].is_monotonic_decreasing)
print("Sum of n_cells:", csv_df["n_cells"].sum())
print("\nBottom 5 types:")
print(csv_df.tail(5).to_string(index=False))

# verify PNG
png_size = os.path.getsize("/work/celltype_counts_bar.png")
print(f"\nPNG size: {png_size/1024:.1f} KB")
