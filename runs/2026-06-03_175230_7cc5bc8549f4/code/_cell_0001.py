
import json
import urllib.request

# Fetch all marmoset (NCBITaxon:9483 = Callithrix jacchus) datasets from CellxGene
url = "https://api.cellxgene.cziscience.com/curation/v1/datasets?organism_ontology_term_id=NCBITaxon:9483"
with urllib.request.urlopen(url) as response:
    datasets = json.loads(response.read())

print(f"Total marmoset datasets on CellxGene: {len(datasets)}")
for d in datasets:
    tissues = [t.get('label','') for t in d.get('tissue', [])]
    title = d.get('title', d.get('dataset_id',''))
    cell_count = d.get('cell_count', 0)
    collection_id = d.get('collection_id', '')
    dataset_id = d.get('dataset_id','')
    assets = d.get('assets', [])
    file_sizes = [(a.get('filetype'), a.get('filesize', 0)//1e9) for a in assets]
    print(f"\n  ID: {dataset_id}")
    print(f"  Collection: {collection_id}")
    print(f"  Title: {title}")
    print(f"  Cells: {cell_count:,}")
    print(f"  Tissues: {tissues}")
    print(f"  Files: {file_sizes}")
