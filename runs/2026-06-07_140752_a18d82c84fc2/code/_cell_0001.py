import urllib.request
url="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=PMC9279161&rettype=full&retmode=xml"
req=urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0 lab-bot"})
xml=urllib.request.urlopen(req, timeout=60).read().decode("utf-8","replace")
print(len(xml))
import re
# strip tags for searching
text=re.sub(r"<[^>]+>"," ",xml)
text=re.sub(r"\s+"," ",text)
print(len(text))
