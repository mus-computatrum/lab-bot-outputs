
# Now I have clear picture:
# 1. Collection 4dca242c = Jorstad+Krienen 2023 Science - "Comparative transcriptomics reveals human-specific cortical features"
#    → Marmoset MTG, 75,861 cells, 0.49 GB, Bakken+Krienen at Allen Institute
# 2. Collection 367d95c0 = Bakken 2021 Nature M1 motor cortex - ~21k marmoset cells, split 3 files

# The user mentioned "Krienen et al. 2023" - that's Jorstad+Krienen 2023 (Krienen is 6th author)
# The user mentioned "Bakken et al. 2021" - that's Bakken 2021 M1

# WINNER: Jorstad/Krienen 2023 MTG 
# - Cortical (MTG, comparable to Tasic 2018 V1/ALM)
# - Allen Institute = clean taxonomy
# - 75k cells at 0.49 GB - manageable
# - License: Science papers use CC BY-NC (need to verify)

# Get all datasets in the Great Apes MTG collection (4dca242c)
coll_ds = [d for d in datasets if d.get('collection_id') == '4dca242c-d302-4dba-a68f-4c61e7bad553']
print(f"Datasets in Jorstad/Krienen 2023 collection:")
for d in coll_ds:
    org = [o['label'] for o in d.get('organism',[])]
    cells = d.get('cell_count',0)
    title = d.get('title','')
    did = d.get('dataset_id','')
    for a in d.get('assets',[]):
        url = a.get('url','')
        size_gb = a.get('filesize',0)/1e9
        print(f"  [{org[0] if org else '?'}] {cells:,} cells | {size_gb:.2f} GB | {title}")
        print(f"    URL: {url}")
        print(f"    dataset_id: {did}")
