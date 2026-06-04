
# Verify file on disk
import os
fsize = os.path.getsize(out_path)
print(f"File size: {fsize} bytes")

# Quick sanity check: re-read
df_check = pd.read_csv(out_path)
print(df_check)
print(f"\nColumns: {df_check.columns.tolist()}")
assert list(df_check.columns) == ["supertype", "n_cells_in_visp", "fraction_of_visp_sst"]
assert len(df_check) == 10
print("\n✓ Validation passed")
