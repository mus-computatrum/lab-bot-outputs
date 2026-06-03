
# Let's take a more targeted approach - look at the largest cortex datasets
# and specifically look for collections from Bakken 2021 or Krienen 2023
import json

# First let's look for datasets by the known collection IDs
# Bakken 2021 is part of the BICCN M1 collection
# Let me search by looking at collections with marmoset + cortex

collections_with_marmoset_cortex = {}
for d in datasets:
    tissues = [t.get('label','').lower() for t in d.get('tissue', [])]
    title = d.get('title', '').lower()
    cell_count = d.get('cell_count', 0)
    collection_id = d.get('collection_id', '')
    cortex_keywords = ['cortex', 'motor', 'frontal', 'prefrontal', 'parietal', 'temporal', 'visual', 'somatosensory', 'cingulate']
    is_cortex = any(kw in ' '.join(tissues) or kw in title for kw in cortex_keywords)
    if is_cortex:
        if collection_id not in collections_with_marmoset_cortex:
            collections_with_marmoset_cortex[collection_id] = {'total_cells': 0, 'datasets': 0, 'example_title': title}
        collections_with_marmoset_cortex[collection_id]['total_cells'] += cell_count
        collections_with_marmoset_cortex[collection_id]['datasets'] += 1

# Sort by total cells
sorted_colls = sorted(collections_with_marmoset_cortex.items(), key=lambda x: -x[1]['total_cells'])
print("Collections with marmoset cortex data (sorted by total cells):")
for coll_id, info in sorted_colls[:15]:
    print(f"  {coll_id}: {info['total_cells']:,} cells across {info['datasets']} datasets | ex: {info['example_title'][:80]}")
