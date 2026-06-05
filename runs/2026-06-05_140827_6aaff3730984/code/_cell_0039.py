
# Final inventory check — all deliverables present
import os
import glob

print("=== FINAL /work/ DELIVERABLES ===\n")

categories = {
    "Figures": ["fig*.png"],
    "Data tables": ["*.csv"],
    "NumPy/sparse arrays": ["*.npy", "*.npz"],
    "Report": ["report.md"],
}

for cat, patterns in categories.items():
    print(f"── {cat} ──")
    files = []
    for pat in patterns:
        files.extend(glob.glob(f'/work/{pat}'))
    for fp in sorted(files):
        sz = os.path.getsize(fp)
        sz_str = f"{sz/1e6:.1f} MB" if sz > 1e6 else f"{sz/1e3:.0f} KB"
        print(f"  {os.path.basename(fp):<45} {sz_str}")
    print()

# Verify figures were saved properly
print("Checking figure dimensions:")
import matplotlib.pyplot as plt
from PIL import Image
for fig_path in sorted(glob.glob('/work/fig*.png')):
    img = Image.open(fig_path)
    print(f"  {os.path.basename(fig_path)}: {img.size[0]}×{img.size[1]} px")
