import os
print("staged exists:", os.path.exists("/work/staged"))
if os.path.exists("/work/staged"):
    print(os.listdir("/work/staged"))
print("work:", os.listdir("/work")[:50])
