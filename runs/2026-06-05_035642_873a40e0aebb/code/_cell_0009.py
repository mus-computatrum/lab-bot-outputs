
import os
os.environ["NUMBA_DISABLE_JIT"] = "1"
import anndata as ad
import scanpy as sc
import pandas as pd

print("Libraries imported successfully")
print("scanpy version:", sc.__version__)
