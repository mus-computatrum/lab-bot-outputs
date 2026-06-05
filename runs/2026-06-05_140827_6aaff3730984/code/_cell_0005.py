
# Inspect skeleton structure more deeply
sample_skel = skeletons[sample_key]
print("Keys:", list(sample_skel.keys()))
print(f"\nmeta: {sample_skel['meta']}")
print(f"\nvertices shape: {np.array(sample_skel['vertices']).shape}")
print(f"edges shape: {np.array(sample_skel['edges']).shape}")
print(f"compartment unique: {np.unique(sample_skel['compartment'])}")
print(f"compartment (first 20): {sample_skel['compartment'][:20]}")
print(f"\nFirst few vertices (nm coords):")
print(np.array(sample_skel['vertices'])[:5])
print(f"\nRoot vertex index: {sample_skel['root']}")
print(f"Root vertex (soma): {np.array(sample_skel['vertices'])[sample_skel['root']]}")

# Check all 10 skeleton root IDs
print("\nAll 10 skeleton root IDs:")
for k in skeletons.keys():
    s = skeletons[k]
    meta = s['meta']
    verts = np.array(s['vertices'])
    comps = np.array(s['compartment'])
    print(f"  {k}: {len(verts)} vertices, soma=({meta['soma_pt_x']:.0f},{meta['soma_pt_y']:.0f},{meta['soma_pt_z']:.0f}) nm, compartments={np.unique(comps)}")
