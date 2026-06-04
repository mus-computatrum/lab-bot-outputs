
# Let me check all available taxonomy metadata files
tax_base = "/data/yao2023-wmb-10x/_abc_cache/metadata/WMB-taxonomy/20231215"
print("WMB-taxonomy metadata files:")
for f in os.listdir(tax_base):
    size = os.path.getsize(os.path.join(tax_base, f))
    print(f"  {f}  ({size/1e6:.1f} MB)")
