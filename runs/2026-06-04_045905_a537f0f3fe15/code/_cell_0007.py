# No space for allensdk full install. Let's try a direct approach.
# Check if allensdk is partially available
import sys
sys.path.insert(0, '/work/pylib')

# Check what's available
try:
    import allensdk
    print("allensdk version:", allensdk.__version__)
except Exception as e:
    print("allensdk not available:", e)

# Check what IS installed
import pkg_resources
installed = [p.project_name for p in pkg_resources.working_set]
allen_pkgs = [p for p in installed if 'allen' in p.lower() or 'brain' in p.lower()]
print("Allen-related packages:", allen_pkgs)
