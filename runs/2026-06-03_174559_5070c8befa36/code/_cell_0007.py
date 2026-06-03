
import numpy as np
import scipy.sparse as sp

# Work on the SST subset (already defined earlier in the session)
# sst object has raw counts in .X

# Normalize: CPM then log1p (manual, avoids any scanpy issues)
X = sst.X.copy()
if sp.issparse(X):
    X = X.toarray()

# CPM: divide each cell by its total, multiply by 1e4
cell_totals = X.sum(axis=1, keepdims=True)
X_norm = X / cell_totals * 1e4

# log1p
X_log = np.log1p(X_norm)

print("Normalization done.")
print(f"  X_log shape: {X_log.shape}")
print(f"  X_log min: {X_log.min():.3f}, max: {X_log.max():.3f}")
print(f"  Sample mean (Calb2): {X_log[:, list(sst.var_names).index('Calb2')].mean():.4f}")
