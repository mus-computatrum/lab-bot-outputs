# This looks like it might be Visual Behavior, not Visual Coding.
# Check the ophys_experiment_data folder for NWBs
nwbs = sorted(glob.glob('/data/abo-visualcoding-v1/ophys_experiment_data/*.nwb'))
print(f"NWB files present: {len(nwbs)}")
for n in nwbs[:5]:
    sz = os.path.getsize(n)
    print(f"  {os.path.basename(n)}  ({sz/1e6:.0f} MB)")
