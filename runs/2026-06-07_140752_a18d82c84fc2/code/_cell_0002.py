import re
def ctx(pat, n=320, k=6):
    hits=[m.start() for m in re.finditer(pat, text, re.I)]
    print(f"=== '{pat}' : {len(hits)} hits ===")
    for s in hits[:k]:
        print("..."+text[max(0,s-n):s+n]+"...\n")

for p in [r"\bmice\b", r"\bmouse\b", r"Sst-Reln", r"Martinotti", r"five subclasses|5 subclasses", r"11 types|eleven types", r"35 subtypes|thirty-five subtypes", r"three-level"]:
    ctx(p)
    print("-"*80)
