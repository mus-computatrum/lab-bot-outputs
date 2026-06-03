
# Filter for cortex datasets with reasonable cell counts (>10k cells)
# and cortical tissue labels
cortex_keywords = ['cortex', 'cortical', 'motor', 'visual', 'frontal', 'temporal', 
                   'parietal', 'prefrontal', 'somatosensory']

cortex_datasets = []
for d in datasets:
    tissues = [t.get('label','').lower() for t in d.get('tissue', [])]
    title = d.get('title', '').lower()
    cell_count = d.get('cell_count', 0)
    is_cortex = any(kw in ' '.join(tissues) or kw in title for kw in cortex_keywords)
    if is_cortex and cell_count > 5000:
        cortex_datasets.append(d)

print(f"Cortex marmoset datasets (>5k cells): {len(cortex_datasets)}")
for d in sorted(cortex_datasets, key=lambda x: -x.get('cell_count',0)):
    tissues = [t.get('label','') for t in d.get('tissue', [])]
    title = d.get('title', d.get('dataset_id',''))
    cell_count = d.get('cell_count', 0)
    collection_id = d.get('collection_id', '')
    dataset_id = d.get('dataset_id','')
    assets = d.get('assets', [])
    file_info = [(a.get('filetype'), round(a.get('filesize', 0)/1e9, 2)) for a in assets]
    print(f"\n  ID: {dataset_id}")
    print(f"  Collection: {collection_id}")
    print(f"  Title: {title}")
    print(f"  Cells: {cell_count:,}")
    print(f"  Tissues: {tissues[:5]}")
    print(f"  Files: {file_info}")
