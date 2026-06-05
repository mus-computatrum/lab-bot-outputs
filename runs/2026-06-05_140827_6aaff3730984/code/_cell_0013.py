
import scipy.sparse as sp
from tqdm.auto import tqdm

# Step 2: Build sparse connectivity matrix from synapse files
# Each file: *_post.parquet → incoming synapses for that neuron
# We only want synapses where BOTH pre and post are in the proofread set

syn_files = sorted(glob.glob('/data/microns-minnie65/synapses/*_post.parquet'))

# For memory efficiency, build COO arrays
rows_list = []   # post index
cols_list = []   # pre index
data_count = []  # synapse count
data_size  = []  # total synapse size

pr_id_set = set(root_ids)

n_loaded = 0
n_within = 0
for fpath in syn_files:
    post_id = os.path.basename(fpath).replace('_post.parquet', '')
    if post_id not in id_to_idx:
        continue
    
    df = pd.read_parquet(fpath, columns=['pre_pt_root_id', 'post_pt_root_id', 'size', 'valid'])
    df = df[df['valid'] == True]
    
    # Filter to pre synapses from proofread neurons only
    df['pre_id_str'] = df['pre_pt_root_id'].astype(str)
    df_within = df[df['pre_id_str'].isin(pr_id_set)]
    
    if len(df_within) > 0:
        post_idx = id_to_idx[post_id]
        for _, row in df_within.iterrows():
            pre_idx = id_to_idx[str(row['pre_id_str'])]
            rows_list.append(post_idx)   # post
            cols_list.append(pre_idx)    # pre
            data_size.append(float(row['size']))
        n_within += len(df_within)
    
    n_loaded += 1

print(f"Loaded {n_loaded} synapse files")
print(f"Within-proofread synapses: {n_within}")
