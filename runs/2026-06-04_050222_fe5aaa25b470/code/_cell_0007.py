import struct, os

nwb_dst = "/work/sub17797_ses4_scan9_patched.nwb"
actual_size = os.path.getsize(nwb_dst)
print(f"Actual size: {actual_size:,}  ({hex(actual_size)})")

# Patch bytes 40-47 with the actual file size (little-endian uint64)
with open(nwb_dst, "r+b") as f:
    f.seek(40)
    old_val = struct.unpack('<Q', f.read(8))[0]
    print(f"Old EOF field: {old_val:,}  ({hex(old_val)})")
    f.seek(40)
    f.write(struct.pack('<Q', actual_size))
    f.seek(40)
    new_val = struct.unpack('<Q', f.read(8))[0]
    print(f"New EOF field: {new_val:,}  ({hex(new_val)})")

print("Patch applied!")
