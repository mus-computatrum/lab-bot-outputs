# Fix pynwb cache dir issue by setting HOME to /work
import os
os.environ['HOME'] = '/work'
os.environ['XDG_CACHE_HOME'] = '/work/.cache'
os.makedirs('/work/.cache', exist_ok=True)

# Also mock SimpleITK
import sys
from unittest.mock import MagicMock
if 'SimpleITK' not in sys.modules:
    sys.modules['SimpleITK'] = MagicMock()

# Now try again
try:
    from allensdk.core.brain_observatory_cache import BrainObservatoryCache
    print("BrainObservatoryCache OK!")
except Exception as e:
    print(f"Still failing: {e}")
    import traceback
    traceback.print_exc()
