# Hrvatin 2019 eLife - data availability
for url in ["https://elifesciences.org/articles/48089"]:
    h = fetch(url)
    print(url, "len", len(h))
    secs, txt = find_section(h, "Data availability")
    for s in secs[:2]:
        print("----\n", s[:1600])
    # also GEO accessions mentioned
    for acc in set(re.findall(r'GSE\d+', txt)):
        print("ACC:", acc)