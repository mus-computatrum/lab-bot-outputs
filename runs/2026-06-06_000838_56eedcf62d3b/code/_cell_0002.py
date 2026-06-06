
import os
size = os.path.getsize("/work/bugeon_methods_extract.md")
print(f"File size: {size} bytes")

with open("/work/bugeon_methods_extract.md") as f:
    text = f.read()
print(f"Characters: {len(text)}")
print("\n--- FULL FILE ---\n")
print(text)
