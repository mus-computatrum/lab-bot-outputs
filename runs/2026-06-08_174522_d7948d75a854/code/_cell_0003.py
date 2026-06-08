# Full GEO series record incl supplementary files
geo_full = fetch("https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE232200&targ=self&form=text&view=full")
for line in geo_full.splitlines():
    if 'supplementary' in line.lower() or 'sample_id' in line.lower() or 'platform' in line.lower():
        print(line)

# Sample details
for gsm in ["GSM7317753","GSM7317754"]:
    rec = fetch(f"https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={gsm}&targ=self&form=text&view=brief")
    print(f"\n=== {gsm} ===")
    for line in rec.splitlines():
        if any(k in line for k in ['title','source','organism','supplementary','library','instrument','characteristics']):
            print(line)