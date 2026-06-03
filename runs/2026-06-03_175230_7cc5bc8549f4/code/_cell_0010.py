
# Get the dataset-level metadata from CellxGene for license info
import urllib.request, json

url = "https://api.cellxgene.cziscience.com/curation/v1/datasets/b7a0cd4e-77c2-4ae6-9eb7-8945e27e93b8"
with urllib.request.urlopen(url) as r:
    ds = json.loads(r.read())

print("Dataset full metadata:")
print(f"  title: {ds.get('title','')}")
print(f"  collection_id: {ds.get('collection_id','')}")
print(f"  schema_version: {ds.get('schema_version','')}")
# Look for license info
print(f"  is_primary_data: {ds.get('is_primary_data','')}")
print(f"  cell_count: {ds.get('cell_count','')}")
print(f"  assay: {ds.get('assay','')}")
print(f"  organism: {ds.get('organism','')}")
print(f"  tissue: {ds.get('tissue','')}")
print(f"  publication_citation: {ds.get('publication_citation','')}")
print(f"\nFull keys: {list(ds.keys())}")
