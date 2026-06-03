
import scanpy as sc
import scipy.sparse as sp

# Confirm .X is raw counts (large integers, no negatives)
sst_counts = sst.copy()

# Normalize to 10k then log1p
sc.pp.normalize_total(sst_counts, target_sum=1e4)
sc.pp.log1p(sst_counts)

# Sanity check
print("After normalize+log1p:")
print("  X min:", sst_counts.X.min())
print("  X max:", sst_counts.X.max())
print("  X dtype:", sst_counts.X.dtype)

# Get the marker gene indices
markers = ['Calb2', 'Crh', 'Hpse', 'Nos1', 'Pdyn', 'Chrna2']
marker_idx = [list(sst_counts.var_names).index(m) for m in markers]
print("\nMarker indices:", marker_idx)
