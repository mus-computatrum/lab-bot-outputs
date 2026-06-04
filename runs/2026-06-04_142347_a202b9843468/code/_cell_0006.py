
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── RESULT: All 4 requested genes are ABSENT from this panel ──
# The Vizgen MERFISH Mouse Brain Receptor Map is a receptor-focused panel
# (483 real genes, all receptors/signaling). Calb2, Crh, Nos1, Pdyn are
# neuropeptides / calcium-binding proteins — not receptors.

# Identify the closest available receptor-panel proxies for each SST marker
# Calb2+  SST neurons express Sstr2 prominently
# Crh     → Crhr1 (primary CRH receptor in cortex), Crhr2
# Nos1    → Chodl/large SST; closest receptor is Npy1r or Sstr1 (both present)
# Pdyn    → Oprk1 (kappa-opioid receptor, dynorphin's primary target)
proxy_map = {
    "Calb2":  ("Sstr2",  "SST receptor 2 — proxy for Calb2+ SST cells"),
    "Crh":    ("Crhr1",  "CRH receptor 1 — cognate receptor for Crh"),
    "Nos1":   ("Sstr1",  "SST receptor 1 — proxy for Nos1/Chodl-like SST cells"),
    "Pdyn":   ("Oprk1",  "Kappa-opioid receptor — primary target of Pdyn"),
}

# Build the summary CSV for the 4 requested genes (all absent)
requested_genes = ["Calb2", "Crh", "Nos1", "Pdyn"]
rows = []
for g in requested_genes:
    rows.append({
        "gene": g,
        "n_transcripts": 0,
        "mean_x": np.nan,
        "mean_y": np.nan,
        "std_x": np.nan,
        "std_y": np.nan,
        "note": f"NOT IN PANEL — receptor-map dataset; suggested proxy: {proxy_map[g][0]} ({proxy_map[g][1]})"
    })

summary_df = pd.DataFrame(rows)
summary_df.to_csv("/work/vizgen_sst_marker_summary.csv", index=False)
print("Saved /work/vizgen_sst_marker_summary.csv")
print(summary_df[["gene","n_transcripts","note"]].to_string(index=False))
