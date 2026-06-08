for acc,nnn in [('GSE232200','GSE232nnn'),('GSE136802','GSE136nnn')]:
    url=f"https://ftp.ncbi.nlm.nih.gov/geo/series/{nnn}/{acc}/suppl/filelist.txt"
    print("="*70); print(url)
    print(listing(url))

# per-sample for GSE232200 bioreps
for gsm,nnn in [('GSM7317753','GSM7317nnn'),('GSM7317754','GSM7317nnn')]:
    url=f"https://ftp.ncbi.nlm.nih.gov/geo/samples/{nnn}/{gsm}/suppl/"
    print("="*70); print(url)
    print(listing(url)[:2000])
