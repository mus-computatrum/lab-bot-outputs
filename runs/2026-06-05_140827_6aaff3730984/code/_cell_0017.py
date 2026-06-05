
# Step 5: Skeleton-based dendrodendritic proximity analysis for the 10 pre-downloaded neurons
# Compartment labels: 1=soma, 2=axon, 3=dendrite

# Build per-skeleton DataFrames
skel_data = {}
for rid, skel in skeletons.items():
    verts = np.array(skel['vertices'])   # nm
    comps = np.array(skel['compartment'])
    meta  = skel['meta']
    skel_data[rid] = {
        'vertices_nm': verts,
        'compartment': comps,
        'soma_nm': np.array([meta['soma_pt_x'], meta['soma_pt_y'], meta['soma_pt_z']]),
        'dendrite_verts': verts[comps == 3],   # compartment=3 → dendrite
        'axon_verts': verts[comps == 2],       # compartment=2 → axon
        'soma_verts': verts[comps == 1],       # compartment=1 → soma
    }
    print(f"{rid}: soma={verts[comps==1].shape[0]} verts, "
          f"dendrite={verts[comps==3].shape[0]} verts, "
          f"axon={verts[comps==2].shape[0]} verts")

skel_ids = list(skel_data.keys())
print(f"\n10 skeletons: {skel_ids}")
