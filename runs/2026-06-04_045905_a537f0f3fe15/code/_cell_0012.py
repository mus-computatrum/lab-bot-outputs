# Great structure! Let's examine the key fields we need
with h5py.File(nwb_path, 'r') as f:
    # Get genotype/cre line and targeted structure
    genotype = f['general/subject/genotype'][()].decode()
    targeted_structure = f['general/targeted_structure'][()].decode()
    exp_id = f['general/ophys_experiment_id'][()].decode()
    session_type = f['general/session_type'][()].decode()
    
    print(f"Experiment ID: {exp_id}")
    print(f"Genotype: {genotype}")
    print(f"Targeted structure: {targeted_structure}")
    print(f"Session type: {session_type}")
    
    # Check drifting gratings stimulus
    dg = f['stimulus/presentation/drifting_gratings_stimulus']
    print("\nDrifting gratings dataset keys:")
    for k in dg.keys():
        v = dg[k]
        if isinstance(v, h5py.Dataset):
            print(f"  {k}: {v.shape} {v.dtype} — first 5: {v[:5]}")
