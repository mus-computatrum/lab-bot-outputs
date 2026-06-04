# allensdk 2.16.2 is available but has import issues. Let's try importing submodules directly.
try:
    from allensdk.core.brain_observatory_cache import BrainObservatoryCache
    print("BrainObservatoryCache OK")
except Exception as e:
    print(f"Error: {e}")
    # Try to see what the actual problem is
    import traceback
    traceback.print_exc()
