import numpy as np

COUNT_CSV = '/data/gouwens2020-patchseq/transcriptome/20200513_Mouse_PatchSeq_Release_count.v2/20200513_Mouse_PatchSeq_Release_count.v2.csv'

# --- Filter metadata to SST cells ---
sst_meta = meta[meta['corresponding_AIT2.3.1_alias'].str.startswith('Sst', na=False)].copy()
print(f"SST cells in metadata: {len(sst_meta)}")
print(f"SST t-types: {sst_meta['corresponding_AIT2.3.1_alias'].nunique()}")
print(sst_meta['corresponding_AIT2.3.1_alias'].value_counts())
