
# Let's look at collection 283d65eb more carefully - it has 66 datasets and 8M cells
# This looks like the Krienen marmoset brain atlas
# Let's also search for datasets that have "marmoset" or "callithrix" in title

# Check 283d65eb collection
coll_283 = [d for d in datasets if d.get('collection_id') == '283d65eb-dd53-496d-adb7-7570c7caa443']
print(f"Collection 283d65eb: {len(coll_283)} datasets")
print("\nSample titles:")
for d in coll_283[:5]:
    print(f"  - {d.get('title','')} ({d.get('cell_count',0):,} cells)")
    print(f"    tissues: {[t['label'] for t in d.get('tissue',[])[:3]]}")
    assets = d.get('assets', [])
    for a in assets:
        print(f"    file: {a.get('filetype')}, {a.get('filesize',0)/1e9:.2f} GB, url: {a.get('url','')[:80]}")

print("\n\n--- Looking for Bakken/Krienen specific datasets ---")
for d in datasets:
    title = d.get('title', '')
    if any(kw in title.lower() for kw in ['m1', 'motor cortex', 'marmoset', 'callithrix']):
        print(f"\nTitle: {title}")
        print(f"  Collection: {d.get('collection_id')}")
        print(f"  Cells: {d.get('cell_count',0):,}")
        tissues = [t['label'] for t in d.get('tissue',[])]
        print(f"  Tissues: {tissues[:5]}")
        for a in d.get('assets', []):
            print(f"  File: {a.get('filetype')}, {a.get('filesize',0)/1e9:.2f} GB")
