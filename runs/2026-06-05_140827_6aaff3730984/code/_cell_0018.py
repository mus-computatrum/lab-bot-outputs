
# Compute all pairwise dendrodendritic minimum distances for the 10 skeleton neurons
# Also compute soma-soma distances and synapse counts between them

from scipy.spatial.distance import cdist

n_sk = len(skel_ids)
dd_results = []

for i in range(n_sk):
    for j in range(i+1, n_sk):
        rid_a = skel_ids[i]
        rid_b = skel_ids[j]
        
        da = skel_data[rid_a]
        db = skel_data[rid_b]
        
        # Soma-soma distance (nm → µm)
        soma_dist_um = np.linalg.norm(da['soma_nm'] - db['soma_nm']) / 1000.0
        
        # Dendrite-dendrite minimum distance
        if len(da['dendrite_verts']) > 0 and len(db['dendrite_verts']) > 0:
            # Use a subset if too large (for speed)
            da_dend = da['dendrite_verts']
            db_dend = db['dendrite_verts']
            if len(da_dend) > 500: da_dend = da_dend[::len(da_dend)//500]
            if len(db_dend) > 500: db_dend = db_dend[::len(db_dend)//500]
            
            dd_dist = cdist(da_dend, db_dend, 'euclidean').min() / 1000.0  # µm
        else:
            dd_dist = np.nan
        
        # Axon-dendrite minimum distance (proxy for chemical synapse possibility)
        if len(da['axon_verts']) > 0 and len(db['dendrite_verts']) > 0:
            ad_dist_a2b = cdist(da['axon_verts'][::max(1,len(da['axon_verts'])//500)],
                                db['dendrite_verts'][::max(1,len(db['dendrite_verts'])//500)]).min() / 1000.0
        else:
            ad_dist_a2b = np.nan
        
        if len(db['axon_verts']) > 0 and len(da['dendrite_verts']) > 0:
            ad_dist_b2a = cdist(db['axon_verts'][::max(1,len(db['axon_verts'])//500)],
                                da['dendrite_verts'][::max(1,len(da['dendrite_verts'])//500)]).min() / 1000.0
        else:
            ad_dist_b2a = np.nan
        
        # Chemical synapses between this pair (from connectivity matrix)
        idx_a = id_to_idx.get(rid_a, None)
        idx_b = id_to_idx.get(rid_b, None)
        if idx_a is not None and idx_b is not None:
            syn_ab = int(conn_dense[idx_b, idx_a])  # a→b (post=b, pre=a)
            syn_ba = int(conn_dense[idx_a, idx_b])  # b→a
        else:
            syn_ab = syn_ba = 0
        
        dd_results.append({
            'root_id_a': rid_a,
            'root_id_b': rid_b,
            'soma_dist_um': soma_dist_um,
            'dendrite_dendrite_dist_um': dd_dist,
            'axon_dendrite_dist_a2b_um': ad_dist_a2b,
            'axon_dendrite_dist_b2a_um': ad_dist_b2a,
            'syn_a2b': syn_ab,
            'syn_b2a': syn_ba,
            'syn_total': syn_ab + syn_ba,
        })

dd_df = pd.DataFrame(dd_results)
print("Skeleton pair analysis:")
print(dd_df.to_string(index=False))
