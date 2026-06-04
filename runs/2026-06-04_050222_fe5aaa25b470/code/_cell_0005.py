
# Read HDF5 superblock to understand layout and find the stored-EOF field
nwb_path = "/data/microns-functional/sub-17797_ses-4-scan-9_behavior+image+ophys.nwb"

with open(nwb_path, "rb") as f:
    header = f.read(256)

print("Signature:", header[:8])
sb_ver = header[8]
print(f"Superblock version: {sb_ver}")
size_offsets = header[13]
size_lengths  = header[14]
print(f"size_of_offsets={size_offsets}, size_of_lengths={size_lengths}")

import struct

if sb_ver in (0, 1):
    # Fields before addresses:
    # 0-7 sig, 8 sb_ver, 9 free_ver, 10 rg_ver, 11 reserved,
    # 12 shdr_ver, 13 sz_off, 14 sz_len, 15 reserved,
    # 16-17 leaf_K, 18-19 internal_K, 20-23 consistency_flags
    # v1 adds: 24-25 indexed_storage_K, 26-27 reserved2
    base_offset = 20 + 4  # after consistency flags = 24
    if sb_ver == 1:
        base_offset += 4   # extra 4 bytes
    base_addr, = struct.unpack_from('<Q', header, base_offset)
    free_space_addr, = struct.unpack_from('<Q', header, base_offset + 8)
    eof_addr, = struct.unpack_from('<Q', header, base_offset + 16)
    driver_addr, = struct.unpack_from('<Q', header, base_offset + 24)
    print(f"base_addr:       {base_addr:#018x} = {base_addr:,}")
    print(f"free_space_addr: {free_space_addr:#018x}")
    print(f"eof_addr:        {eof_addr:#018x} = {eof_addr:,}")
    print(f"driver_addr:     {driver_addr:#018x}")
    print(f"eof_addr field is at file offset: {base_offset + 16}")
elif sb_ver == 2:
    # v2 superblock: 8+1+1+1+1+1 = 13, then size_of_offsets, size_of_lengths, 
    # file_consistency_flags (1), base_address, superblock_extension_address, 
    # end_of_file_address, root_group_object_header_address
    print("Superblock v2:")
    # offset 13: size_of_offsets; 14: size_of_lengths; 15: file_consistency_flags
    # 16: base_address (sz_off bytes)
    base_offset = 16
    base_addr, = struct.unpack_from('<Q', header, base_offset)
    sb_ext,    = struct.unpack_from('<Q', header, base_offset + 8)
    eof_addr,  = struct.unpack_from('<Q', header, base_offset + 16)
    root_addr, = struct.unpack_from('<Q', header, base_offset + 24)
    print(f"base_addr:  {base_addr:#018x}")
    print(f"sb_ext:     {sb_ext:#018x}")
    print(f"eof_addr:   {eof_addr:#018x} = {eof_addr:,}")
    print(f"root_addr:  {root_addr:#018x}")
    print(f"eof_addr field is at file offset: {base_offset + 16}")
