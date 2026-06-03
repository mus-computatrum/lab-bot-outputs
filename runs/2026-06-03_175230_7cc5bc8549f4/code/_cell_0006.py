
import urllib.request, json

# Get collection metadata from CellxGene API
for coll_id in ['e1fa9900-3fc9-4b57-9dce-c95724c88716', '367d95c0-0eb0-4dae-8276-9407239421ee']:
    url = f"https://api.cellxgene.cziscience.com/curation/v1/collections/{coll_id}"
    with urllib.request.urlopen(url) as r:
        coll = json.loads(r.read())
    print(f"\n=== Collection {coll_id} ===")
    print(f"  Name: {coll.get('name','')}")
    print(f"  Description: {coll.get('description','')[:300]}")
    print(f"  Contact: {coll.get('contact_name','')} <{coll.get('contact_email','')}>")
    print(f"  Links:")
    for link in coll.get('links', []):
        print(f"    {link.get('link_type')}: {link.get('link_url')}")
    print(f"  DOI/Datasets: {len(coll.get('datasets', []))} datasets")
    created = coll.get('created_at','')
    print(f"  Created: {created}")
