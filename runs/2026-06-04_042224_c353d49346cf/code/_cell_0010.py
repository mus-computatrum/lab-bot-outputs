import os
os.environ['NUMBA_DISABLE_JIT'] = '1'

# Build the set of SST sample IDs to use as usecols
sst_ids = set(sst_meta['transcriptomics_sample_id'].tolist())
print(f"SST sample IDs: {len(sst_ids)}")

# Load count matrix — only SST columns (genes are rows, index_col=0)
# pandas usecols with callable: keep col if in sst_ids set (or it's the index)
print("Loading count matrix (SST columns only)…")
counts = pd.read_csv(
    COUNT_CSV,
    index_col=0,
    usecols=lambda col: col == '' or col.strip('"') in sst_ids
)
print("Raw count matrix shape (genes × SST cells):", counts.shape)
print(counts.dtypes.value_counts())
