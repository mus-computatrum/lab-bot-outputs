key_ids = ['32999462','33230336','37824615','35319013','34616075','34616062','36007006',
           '31435019','40185102','35771910','37939194','37824663','37824643','39325889']
s=pubmed_summary(key_ids)
for i in key_ids:
    d=s['result'].get(i,{})
    if not d: 
        print(i,'MISSING'); continue
    doi=[x['value'] for x in d.get('articleids',[]) if x['idtype']=='doi']
    a=d.get('authors',[])
    first=a[0]['name'] if a else ''
    print(f"{i} | {d.get('pubdate')} | {d.get('source')} | {first} | DOI:{doi}")
    print('   ', d.get('title'))
