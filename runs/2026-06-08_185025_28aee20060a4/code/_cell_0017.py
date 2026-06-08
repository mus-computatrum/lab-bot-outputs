import os
def memgb():
    try:
        m=open('/sys/fs/cgroup/memory.max').read().strip()
        lim=float(m)/1e9 if m!='max' else None
    except: lim=None
    tot=os.sysconf('SC_PAGE_SIZE')*os.sysconf('SC_PHYS_PAGES')/1e9
    return lim, tot
print("cgroup limit GB, phys GB:", memgb())
import psutil if False else None
