import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# --- Step 1: Get axon-proofread cell IDs ---
axon_proofread_ids = proof.loc[proof['status_axon'] == True, 'pt_root_id'].unique()
print(f"Axon-proofread cells (status_axon=True): {len(axon_proofread_ids)}")

# --- Step 2: Count outgoing synapses per pre_pt_root_id (restrict to axon-proofread cells) ---
# The synapse table is already from axon-proofread, but let's filter to be exact
syn_ap = syn[syn['pre_pt_root_id'].isin(axon_proofread_ids)]
print(f"Synapses from axon-proofread cells: {len(syn_ap):,} / {len(syn):,} total")

out_counts = (syn_ap
              .groupby('pre_pt_root_id')
              .size()
              .rename('n_outgoing_syn')
              .sort_values(ascending=False))
print(f"\nTop 10 cells by outgoing synapse count:")
print(out_counts.head(10))
