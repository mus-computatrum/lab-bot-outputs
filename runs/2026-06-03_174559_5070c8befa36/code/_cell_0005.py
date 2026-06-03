
import os
os.environ['NUMBA_CACHE_DIR'] = '/work/numba_cache'
os.makedirs('/work/numba_cache', exist_ok=True)

import scanpy as sc
print("scanpy version:", sc.__version__)
