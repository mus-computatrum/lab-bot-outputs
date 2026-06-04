import pandas as pd

# Load metadata first — small file
meta = pd.read_csv('/data/gouwens2020-patchseq/transcriptome/20200625_patchseq_metadata_mouse/20200625_patchseq_metadata_mouse.csv')
print("Shape:", meta.shape)
print("Columns:", meta.columns.tolist())