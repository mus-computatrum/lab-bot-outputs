
# Also check collection 4dca242c (Great apes, marmoset MTG) 
import urllib.request, json
url = "https://api.cellxgene.cziscience.com/curation/v1/collections/4dca242c-d302-4dba-a68f-4c61e7bad553"
with urllib.request.urlopen(url) as r:
    coll = json.loads(r.read())
print(f"Name: {coll.get('name','')}")
print(f"Description: {coll.get('description','')[:500]}")
print(f"Contact: {coll.get('contact_name','')} <{coll.get('contact_email','')}>")
for link in coll.get('links', []):
    print(f"  {link.get('link_type')}: {link.get('link_url')}")
print()
# Also get the dlPFC marmoset dataset metadata
url2 = "https://api.cellxgene.cziscience.com/curation/v1/datasets"
# find the marmoset dlPFC dataset
for d in datasets:
    if d.get('collection_id') == 'e1fa9900-3fc9-4b57-9dce-c95724c88716' and 'Callithrix jacchus' in str(d.get('organism',[])):
        did = d.get('dataset_id')
        print(f"Marmoset dlPFC dataset ID: {did}")
        print(f"Title: {d.get('title')}")
        print(f"Cells: {d.get('cell_count')}")
        for a in d.get('assets',[]):
            print(f"H5AD URL: {a.get('url')}")
            print(f"Size: {a.get('filesize',0)/1e9:.2f} GB")
