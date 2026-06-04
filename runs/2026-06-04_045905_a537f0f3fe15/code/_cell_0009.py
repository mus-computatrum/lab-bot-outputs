# Mock SimpleITK to bypass the import error
import sys
from unittest.mock import MagicMock
sys.modules['SimpleITK'] = MagicMock()

# Now try again
try:
    from allensdk.core.brain_observatory_cache import BrainObservatoryCache
    print("BrainObservatoryCache OK!")
except Exception as e:
    print(f"Still failing: {e}")
    import traceback
    traceback.print_exc()
