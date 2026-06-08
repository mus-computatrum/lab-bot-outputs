# Title of 2023 paper
m = re.search(r'<title>(.*?)</title>', html23)
print("2023 TITLE:", m.group(1) if m else "?")

# GEO record GSE232200
geo = fetch("https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE232200&targ=self&form=text&view=brief")
print("\n--- GEO GSE232200 brief ---")
print(geo[:3000])