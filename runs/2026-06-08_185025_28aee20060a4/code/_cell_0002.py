import urllib.request, ssl, json
ctx = ssl.create_default_context()

def listing(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
        return urllib.request.urlopen(req, timeout=60, context=ctx).read().decode('utf-8', 'replace')
    except Exception as e:
        return f"ERR {e}"

# GEO series suppl listings via HTTPS FTP mirror
for acc, nnn in [('GSE232200','GSE232nnn'),('GSE136802','GSE136nnn')]:
    url = f"https://ftp.ncbi.nlm.nih.gov/geo/series/{nnn}/{acc}/suppl/"
    print("="*70)
    print(url)
    print(listing(url)[:3000])
