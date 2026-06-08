import urllib.request, urllib.parse, json, time
def pubmed_search(term, retmax=20):
    base="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    url=base+"esearch.fcgi?"+urllib.parse.urlencode({"db":"pubmed","term":term,"retmax":retmax,"retmode":"json"})
    with urllib.request.urlopen(url,timeout=30) as r:
        return json.load(r)
def pubmed_summary(ids):
    base="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    url=base+"esummary.fcgi?"+urllib.parse.urlencode({"db":"pubmed","id":",".join(ids),"retmode":"json"})
    with urllib.request.urlopen(url,timeout=30) as r:
        return json.load(r)

for term in ['Hrvatin Sst44','Green Hrvatin somatostatin cortex','Sst44 interneuron',
             'Hrvatin somatostatin interneuron types','Sst44 somatostatin']:
    res=pubmed_search(term)
    print(term,'->',res['esearchresult']['count'],res['esearchresult']['idlist'][:10])
    time.sleep(0.4)
