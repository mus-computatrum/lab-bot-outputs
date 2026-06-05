
import os, subprocess

# Check both data directories
for dataset in ['microns-functional', 'microns-minnie65']:
    path = f'/data/{dataset}'
    print(f"\n{'='*60}")
    print(f"Dataset: {dataset}")
    print(f"{'='*60}")
    if os.path.exists(path):
        result = subprocess.run(['find', path, '-type', 'f', '-ls'], 
                               capture_output=True, text=True)
        print(result.stdout[:5000])
        if result.returncode != 0:
            print("Error:", result.stderr[:500])
    else:
        print(f"Path {path} does not exist")
