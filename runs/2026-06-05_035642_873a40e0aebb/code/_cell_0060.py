
import os
os.environ["NUMBA_DISABLE_JIT"] = "1"

# Check if adata / sst are already in kernel memory
try:
    print("adata shape:", adata.shape)
    print("sst shape:", sst.shape)
    print("adata.X type:", type(adata.X))
    import scipy.sparse
    print("sparse?", scipy.sparse.issparse(adata.X))
except NameError as e:
    print("Need to reload:", e)
