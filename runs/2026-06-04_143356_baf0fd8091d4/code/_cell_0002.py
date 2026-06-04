
import pyarrow.parquet as pq
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

TARGET_GENES = ["Sstr1", "Sstr2", "Crhr1", "Oprk1"]
parquet_dir  = "/data/vizgen-merfish-brain-map/Slice3_Replicate1/detected_transcripts.parquet"

# Confirm these partitions exist
for g in TARGET_GENES:
    p = f"{parquet_dir}/gene={g}"
    exists = os.path.isdir(p)
    print(f"  gene={g}: partition exists={exists}")
