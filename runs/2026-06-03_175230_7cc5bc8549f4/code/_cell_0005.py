
# Let's check the key collections more carefully
# 1. Collection e1fa9900 - dlPFC marmoset 149k cells
# 2. Collection d17249d2 - M1 114k cells (multi-species?)
# 3. Collection 367d95c0 - Bakken 2021 motor cortex

for coll_id in ['e1fa9900-3fc9-4b57-9dce-c95724c88716', 
                 'd17249d2-0e6e-4500-abb8-e6c93fa1ac6f',
                 '367d95c0-0eb0-4dae-8276-9407239421ee',
                 '283d65eb-dd53-496d-adb7-7570c7caa443']:
    coll_ds = [d for d in datasets if d.get('collection_id') == coll_id]
    print(f"\n=== Collection {coll_id} ({len(coll_ds)} datasets) ===")
    for d in coll_ds[:10]:
        title = d.get('title','')
        cells = d.get('cell_count',0)
        org = [o['label'] for o in d.get('organism',[])]
        tissues = [t['label'] for t in d.get('tissue',[])[:3]]
        assets = d.get('assets',[])
        for a in assets:
            url = a.get('url','')
            size_gb = a.get('filesize',0)/1e9
            print(f"  [{cells:,} cells | {org} | {size_gb:.2f}GB] {title}")
            print(f"    url: {url[:90]}")
