final_ids=['37824638','37442136','40196633','40369074']
s=pubmed_summary(final_ids)
for i in final_ids:
    d=s['result'].get(i,{})
    doi=[x['value'] for x in d.get('articleids',[]) if x['idtype']=='doi']
    a=d.get('authors',[]); first=a[0]['name'] if a else ''
    print(f"{i} | {d.get('pubdate')} | {d.get('source')} | {first} | DOI:{doi}")
    print('   ', d.get('title'))
