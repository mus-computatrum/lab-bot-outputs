
# Let's compare both main candidates and check cell type annotations
# Get the collection metadata for dlPFC paper to confirm source publication

import urllib.request, json

# Check the full collection info + DOI for e1fa9900
url = "https://api.cellxgene.cziscience.com/curation/v1/collections/e1fa9900-3fc9-4b57-9dce-c95724c88716"
with urllib.request.urlopen(url) as r:
    coll = json.loads(r.read())
print("=== dlPFC Collection Full Info ===")
print(f"Name: {coll.get('name','')}")
print(f"DOI: {coll.get('doi','')}")
print(f"Publisher Metadata: {json.dumps(coll.get('publisher_metadata', {}), indent=2)[:600]}")

# And the Bakken M1 collection  
url2 = "https://api.cellxgene.cziscience.com/curation/v1/collections/367d95c0-0eb0-4dae-8276-9407239421ee"
with urllib.request.urlopen(url2) as r:
    coll2 = json.loads(r.read())
print("\n=== Bakken M1 Collection Full Info ===")
print(f"Name: {coll2.get('name','')}")
print(f"DOI: {coll2.get('doi','')}")
print(f"Publisher Metadata: {json.dumps(coll2.get('publisher_metadata', {}), indent=2)[:600]}")

# And the Great Apes MTG collection
url3 = "https://api.cellxgene.cziscience.com/curation/v1/collections/4dca242c-d302-4dba-a68f-4c61e7bad553"
with urllib.request.urlopen(url3) as r:
    coll3 = json.loads(r.read())
print("\n=== Great Apes MTG Collection Full Info ===")
print(f"Name: {coll3.get('name','')}")
print(f"DOI: {coll3.get('doi','')}")
print(f"Publisher Metadata: {json.dumps(coll3.get('publisher_metadata', {}), indent=2)[:600]}")
