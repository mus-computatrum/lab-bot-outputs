import struct

nwb_dst = "/work/sub17797_ses4_scan9_patched.nwb"

with open(nwb_dst, "rb") as f:
    raw = f.read(256)

# v0 superblock, size_of_offsets=8
# offset 56+: root group symbol table entry
def u64(buf, off):
    return struct.unpack_from('<Q', buf, off)[0]
def u32(buf, off):
    return struct.unpack_from('<I', buf, off)[0]

link_name_off   = u64(raw, 56)
obj_header_addr = u64(raw, 64)
cache_type      = u32(raw, 72)
reserved        = u32(raw, 76)
btree_addr      = u64(raw, 80)
heap_addr       = u64(raw, 88)

print(f"Root group symbol table entry:")
print(f"  link_name_offset  = {link_name_off}")
print(f"  obj_header_addr   = {obj_header_addr:#018x} = {obj_header_addr:,}")
print(f"  cache_type        = {cache_type}  (1=group)")
print(f"  scratch btree_addr = {btree_addr:#018x} = {btree_addr:,}")
print(f"  scratch heap_addr  = {heap_addr:#018x} = {heap_addr:,}")

actual_size = 31_708_938_240
print(f"\nActual file size: {actual_size:,}")
print(f"obj_header_addr accessible? {obj_header_addr < actual_size}")
print(f"btree_addr      accessible? {btree_addr < actual_size}")
print(f"heap_addr       accessible? {heap_addr < actual_size}")
