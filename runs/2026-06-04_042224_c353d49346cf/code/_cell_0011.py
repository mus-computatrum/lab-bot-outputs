# One cell missing — check which
missing = sst_ids - set(counts.columns)
print("Missing from count matrix:", missing)

# Build cell → ttype mapping
id2ttype = sst_meta.set_index('transcriptomics_sample_id')['corresponding_AIT2.3.1_alias'].to_dict()

# Align: only cells present in both
common_cells = [c for c in counts.columns if c in id2ttype]
print(f"Cells with both count data and metadata: {len(common_cells)}")
counts = counts[common_cells]

# Log1p transform
import numpy as np
log1p_counts = np.log1p(counts.values.astype(np.float32))   # genes × cells
print("log1p matrix shape:", log1p_counts.shape)
