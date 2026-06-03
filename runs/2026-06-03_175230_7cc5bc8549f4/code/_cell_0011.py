
# Find the marmoset dataset entry in the already-fetched datasets list
marmoset_great_apes = None
for d in datasets:
    if d.get('dataset_id') == 'b7a0cd4e-77c2-4ae6-9eb7-8945e27e93b8':
        marmoset_great_apes = d
        break

if marmoset_great_apes:
    print("Keys:", list(marmoset_great_apes.keys()))
    # Look for license info
    for key in ['license', 'is_primary_data', 'mean_genes_per_cell', 'schema_version']:
        print(f"  {key}: {marmoset_great_apes.get(key,'N/A')}")
    
    # Check the dataset_version_id
    print(f"  dataset_version_id: {marmoset_great_apes.get('dataset_version_id','')}")
    
    # Full print
    import json
    print(json.dumps(marmoset_great_apes, indent=2)[:2000])
else:
    print("Dataset not found in cached list")
