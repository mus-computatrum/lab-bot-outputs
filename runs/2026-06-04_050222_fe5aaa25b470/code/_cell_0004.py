
# Check disk space available in /work
import shutil
total, used, free = shutil.disk_usage("/work")
print(f"/work  total={total/1e9:.0f} GB  used={used/1e9:.0f} GB  free={free/1e9:.0f} GB")

total2, used2, free2 = shutil.disk_usage("/data")
print(f"/data  total={total2/1e9:.0f} GB  used={used2/1e9:.0f} GB  free={free2/1e9:.0f} GB")
