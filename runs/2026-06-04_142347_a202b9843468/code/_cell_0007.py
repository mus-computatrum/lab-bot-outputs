
import os
os.environ["MPLCONFIGDIR"] = "/work/.mpl"
os.makedirs("/work/.mpl", exist_ok=True)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Now compute spatial stats for the 4 receptor proxies ──────────────────────
proxy_genes = ["Sstr2", "Crhr1", "Sstr1", "Oprk1"]
target_genes_label = ["Calb2 → Sstr2", "Crh → Crhr1", "Nos1 → Sstr1", "Pdyn → Oprk1"]
colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3"]

# Filter for proxy genes
mask_proxy = pc.is_in(table["gene"], value_set=pa.array(proxy_genes))
df_proxy = table.filter(mask_proxy).to_pandas()
print("Proxy gene counts:")
print(df_proxy["gene"].value_counts())
