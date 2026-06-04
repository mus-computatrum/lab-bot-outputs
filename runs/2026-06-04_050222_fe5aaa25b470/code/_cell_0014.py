
# Inspect raw bytes at root OH address and understand the format
root_oh = 96
raw_hdr = bytes(mm[root_oh:root_oh+64])
print("Raw bytes at root OH (hex):", raw_hdr.hex())
print("As ASCII:", raw_hdr[:10])
print("Version byte:", raw_hdr[0])
print()

# Check if it's actually v2 object header (signature "OHDR")
if raw_hdr[:4] == b'OHDR':
    print("This is a v2 object header!")
else:
    print("Not OHDR sig — v1 format")
    version = raw_hdr[0]
    reserved = raw_hdr[1]
    num_msgs = struct.unpack_from('<H', raw_hdr, 2)[0]
    ref_count = struct.unpack_from('<I', raw_hdr, 4)[0]
    data_size = struct.unpack_from('<I', raw_hdr, 8)[0]
    print(f"  version={version}, reserved={reserved}, num_msgs={num_msgs}, ref_count={ref_count}, data_size={data_size}")
    print(f"  OH data starts at offset {root_oh+16}, size={data_size}")
    # Print first message raw bytes
    msg_raw = bytes(mm[root_oh+16:root_oh+16+40])
    print(f"  First msg raw: {msg_raw.hex()}")
    m_type = struct.unpack_from('<H', msg_raw, 0)[0]
    m_len  = struct.unpack_from('<H', msg_raw, 2)[0]
    print(f"  First msg: type={m_type} (0x{m_type:04x}), len={m_len}")
