
# Clean up the large patched copy — it's 31.7 GB we don't need
import os
patched = "/work/sub17797_ses4_scan9_patched.nwb"
if os.path.exists(patched):
    os.remove(patched)
    print("Deleted patched copy")

mm.close()
fh.close()
print("mmapped file handle closed")
