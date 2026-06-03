
import os
os.environ['NUMBA_DISABLE_JIT'] = '1'
import importlib
import sys

# Remove any partially loaded scanpy modules
for key in list(sys.modules.keys()):
    if 'scanpy' in key or 'numba' in key:
        del sys.modules[key]

import scanpy as sc
print("scanpy version:", sc.__version__)
