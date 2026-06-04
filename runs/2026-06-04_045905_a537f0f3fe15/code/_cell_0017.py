# Now I understand the structure. Let me write a function to:
# 1. Read all 27 NWBs, filter for VISp + Sst-IRES-Cre
# 2. Compute OSI per cell from drifting grating responses

# First, check what all 27 NWBs contain (genotype + area)
nwb_paths = sorted(glob.glob('/data/abo-visualcoding-v1/ophys_experiment_data/*.nwb'))
print(f"Checking {len(nwb_paths)} NWBs for Sst + VISp...")
sst_visp_nwbs = []

for p in nwb_paths:
    eid = int(os.path.basename(p).replace('.nwb',''))
    try:
        with h5py.File(p, 'r') as f:
            geno = f['general/subject/genotype'][()].decode()
            area = f['general/targeted_structure'][()].decode()
            stype = f['general/session_type'][()].decode()
            # Check if drifting gratings present
            has_dg = 'drifting_gratings_stimulus' in f['stimulus/presentation']
    except Exception as e:
        geno, area, stype, has_dg = 'ERR', 'ERR', 'ERR', False
    
    is_sst = 'Sst-IRES-Cre' in geno
    is_visp = 'VISp' == area
    print(f"  {eid}: area={area} sst={is_sst} dg={has_dg} geno={geno[:40]}")
    if is_sst and is_visp and has_dg:
        sst_visp_nwbs.append(p)

print(f"\n→ {len(sst_visp_nwbs)} VISp + Sst-IRES-Cre + drifting_gratings NWBs found")
