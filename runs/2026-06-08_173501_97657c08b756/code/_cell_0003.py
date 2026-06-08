def efetch_abstract(pmid):
    base="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    url=base+"efetch.fcgi?"+urllib.parse.urlencode({"db":"pubmed","id":pmid,"rettype":"abstract","retmode":"text"})
    with urllib.request.urlopen(url,timeout=30) as r:
        return r.read().decode('utf-8','replace')
print(efetch_abstract('37468637')[:2500])
