import os
os.environ["NUMBA_DISABLE_JIT"] = "1"
import anndata
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# List data files to confirm path
import subprocess
result = subprocess.run(["find", "/data/tasic2018-v1", "-type", "f"], capture_output=True, text=True)
print(result.stdout[:3000])
