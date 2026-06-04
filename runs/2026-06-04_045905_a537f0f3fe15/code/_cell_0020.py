# Run across all 11 VISp + Sst-IRES-Cre experiments
all_dfs = []
for p in sst_visp_nwbs:
    print(f"Processing {os.path.basename(p)} ...", end=' ')
    try:
        df = compute_osi_for_experiment(p)
        print(f"{len(df)} cells, OSI mean={df.osi.mean():.3f}")
        all_dfs.append(df)
    except Exception as e:
        print(f"ERROR: {e}")

full_df = pd.concat(all_dfs, ignore_index=True)
print(f"\nTotal records: {len(full_df)}")
print(f"Unique experiments: {full_df.ophys_experiment_id.nunique()}")
print(f"Unique cells: {full_df.cell_specimen_id.nunique()}")
print(full_df.osi.describe())
