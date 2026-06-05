
# Quick check: any non-VISp cells in this V1 object?
print("dissected_region value counts:")
print(adata.obs["dissected_region"].value_counts())

# Also verify files on disk
import os
for f in ["/work/celltype_counts.csv", "/work/celltype_counts_bar.png"]:
    size = os.path.getsize(f)
    print(f"{f}: {size:,} bytes")
