
import os
os.environ["MPLCONFIGDIR"] = "/work/.mpl_cache"

import pyarrow.parquet as pq
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

TARGET_GENES = ["Sstr1", "Sstr2", "Crhr1", "Oprk1"]
parquet_dir  = "/data/vizgen-merfish-brain-map/Slice3_Replicate1/detected_transcripts.parquet"

# ── 1. Read only the 4 gene partitions ────────────────────────────────────────
frames = []
for g in TARGET_GENES:
    part_path = f"{parquet_dir}/gene={g}"
    table = pq.read_table(part_path, columns=["global_x", "global_y"])
    df = table.to_pandas()
    df["gene"] = g
    frames.append(df)
    print(f"  {g}: {len(df):,} transcripts  "
          f"mean_x={df.global_x.mean():.1f}  mean_y={df.global_y.mean():.1f}")

data = pd.concat(frames, ignore_index=True)
print(f"\nTotal rows loaded: {len(data):,}")
