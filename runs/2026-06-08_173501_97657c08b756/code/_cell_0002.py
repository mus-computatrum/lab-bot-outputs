ids = ['37468637','31545165']
s=pubmed_summary(ids)
for i in ids:
    d=s['result'][i]
    auth=', '.join(a['name'] for a in d.get('authors',[])[:5])
    print(i, d.get('pubdate'), '|', d.get('source'))
    print('  ', d.get('title'))
    print('  ', auth)
    print('  DOI:', [x['value'] for x in d.get('articleids',[]) if x['idtype']=='doi'])
    print()
# Also check Hrvatin Sst44 top
res=pubmed_search('Hrvatin Sst44',retmax=15)
s2=pubmed_summary(res['esearchresult']['idlist'])
print("==== Hrvatin Sst44 results ====")
for i in res['esearchresult']['idlist']:
    d=s2['result'][i]
    print(i, d.get('pubdate'),'|',d.get('source'),'|',d.get('title')[:90])
