
# Check synapse file structure and look for repeat stimulus conditions
import pandas as pd, numpy as np

# Sample one synapse file
syn_sample = pd.read_parquet('/data/microns-minnie65/synapses/864691135686494647_post.parquet')
print("Synapse file shape:", syn_sample.shape)
print("Columns:", syn_sample.columns.tolist())
print("\nFirst 5 rows:")
print(syn_sample.head(5).to_string())
print(f"\nSample of pre_pt_root_id values: {syn_sample['pre_pt_root_id'].head(5).values}")

# Check if root IDs in proofreading table match synapse filenames
pr = pd.read_parquet('/data/microns-minnie65/proofreading_status_and_strategy.parquet')
pr_ids = set(pr['pt_root_id'].astype(str))
syn_files = [os.path.basename(f).replace('_post.parquet','') 
             for f in __import__('glob').glob('/data/microns-minnie65/synapses/*.parquet')]
syn_ids = set(syn_files)
print(f"\nProofread neuron count: {len(pr_ids)}")
print(f"Synapse files count: {len(syn_ids)}")
print(f"Overlap: {len(pr_ids & syn_ids)}")
