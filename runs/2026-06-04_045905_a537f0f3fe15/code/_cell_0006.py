# This JSON seems to be a mix of Visual Behavior and Visual Coding.
# The NWB IDs on disk are classic Visual Coding IDs (5xxM range).
# We need to use the AllenSDK BrainObservatoryCache pointing at the local cache.
# Let's try to set up the SDK with the local manifest.

import os
os.environ['NUMBA_DISABLE_JIT'] = '1'

# Try AllenSDK
try:
    from allensdk.core.brain_observatory_cache import BrainObservatoryCache
    print("BrainObservatoryCache import OK")
except ImportError as e:
    print(f"Import error: {e}")
    # Try to install
    import subprocess
    result = subprocess.run(['pip', 'install', 'allensdk', '--target', '/work/pylib', '-q'], 
                           capture_output=True, text=True)
    print(result.stdout[-500:] if result.stdout else "")
    print(result.stderr[-500:] if result.stderr else "")
