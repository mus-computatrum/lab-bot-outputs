# Check what experiment IDs are present as NWBs
nwb_ids = [int(os.path.basename(n).replace('.nwb','')) for n in nwbs]
print("NWB IDs on disk:", nwb_ids)

# The ophys_experiments.json doesn't seem to have cre_line / targeted_structure fields we need.
# Let's check a few more examples from experiments JSON for structure
for exp in experiments_raw[:10]:
    ts = exp.get('targeted_structure', {})
    if isinstance(ts, dict):
        ts_name = ts.get('acronym', ts.get('name', '?'))
    else:
        ts_name = str(ts)
    print(f"  id={exp['id']} stim={exp.get('stimulus_name','')} area={ts_name}")
