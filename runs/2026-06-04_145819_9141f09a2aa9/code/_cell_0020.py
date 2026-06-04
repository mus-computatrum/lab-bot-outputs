
# Check the views directory for taxonomy
views_path = tax_base + "/views"
print("Views in WMB-taxonomy:")
for f in os.listdir(views_path):
    size = os.path.getsize(os.path.join(views_path, f))
    print(f"  {f}  ({size/1e6:.1f} MB)")
