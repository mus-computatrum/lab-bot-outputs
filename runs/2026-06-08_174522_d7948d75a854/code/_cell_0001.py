import urllib.request, re
def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (research; lab-bot)'})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            return r.read().decode('utf-8', 'replace')
    except Exception as e:
        return f"ERR {e}"

def find_section(html, keyword):
    text = re.sub(r'<[^>]+>', ' ', html)
    text = re.sub(r'\s+', ' ', text)
    idxs=[m.start() for m in re.finditer(keyword, text, re.I)]
    return [text[i:i+1500] for i in idxs], text

html23 = fetch("https://www.nature.com/articles/s41586-023-06357-1")
print("len", len(html23))
secs, text23 = find_section(html23, "Data availability")
for s in secs[:3]:
    print("----\n", s, "\n")