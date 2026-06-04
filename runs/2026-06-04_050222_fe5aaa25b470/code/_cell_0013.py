
# Manual HDF5 v0 superblock + B-tree v1 navigator
import struct, mmap

nwb_dst = "/work/sub17797_ses4_scan9_patched.nwb"
ACTUAL_SIZE = 31_708_938_240
UNDEF = 0xffffffffffffffff

# Memory-map the file for fast random access
fh = open(nwb_dst, "rb")
mm = mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_READ)

def u64(off): return struct.unpack_from('<Q', mm, off)[0]
def u32(off): return struct.unpack_from('<I', mm, off)[0]
def u16(off): return struct.unpack_from('<H', mm, off)[0]
def u8(off):  return mm[off]
def sig(off, n): return mm[off:off+n]

def safe(addr): return 0 <= addr < ACTUAL_SIZE

# Decode object header v1 messages at a given address, return dict of messages
def read_oh_v1(addr):
    """Parse object header version 1; return list of (msg_type, data_start, data_len)."""
    assert sig(addr, 1) != b'\x02', "looks like v2 OH"
    version = u8(addr)
    # header: version(1), reserved(1), num_messages(2), ref_count(4), data_size(4), padding(4) = 16 bytes
    num_msg = u16(addr + 2)
    data_size = u32(addr + 8)
    messages = []
    pos = addr + 16
    end = pos + data_size
    while pos < end:
        msg_type = u16(pos)
        data_len = u16(pos + 2)
        flags    = u8(pos + 4)
        # 3 bytes reserved
        data_start = pos + 8
        if msg_type == 0 and data_len == 0:
            break  # NULL terminator
        messages.append((msg_type, data_start, data_len))
        pos += 8 + data_len
        if pos % 8:
            pos += 8 - (pos % 8)
    return messages

# Decode a Symbol Table message (msg_type=17 = 0x11) → (btree_addr, heap_addr)
def decode_symtable_msg(data_start):
    btree = u64(data_start)
    heap  = u64(data_start + 8)
    return btree, heap

# Read a Local Heap to build name→offset lookup
def read_local_heap(heap_addr):
    assert sig(heap_addr, 4) == b'HEAP', f"Expected HEAP at {heap_addr}"
    version   = u8(heap_addr + 4)
    data_size = u64(heap_addr + 8)
    free_head = u64(heap_addr + 16)
    data_addr = u64(heap_addr + 24)
    raw = mm[data_addr: data_addr + data_size]
    return raw  # names are null-terminated strings at offsets

def heap_name(heap_raw, offset):
    end = heap_raw.index(b'\x00', offset)
    return heap_raw[offset:end].decode('utf-8', errors='replace')

# Read a B-tree v1 (type 0 = group) and collect (key, child_addr) pairs
def read_btree_leaves(btree_addr):
    children = []
    def walk(addr):
        assert sig(addr, 4) == b'TREE', f"Expected TREE at {addr}"
        node_type = u8(addr + 4)
        level     = u8(addr + 5)
        entries   = u16(addr + 6)
        left_sib  = u64(addr + 8)
        right_sib = u64(addr + 16)
        pos = addr + 24
        keys = []
        childs = []
        for i in range(entries + 1):
            keys.append(u64(pos)); pos += 8
            if i < entries:
                childs.append(u64(pos)); pos += 8
        if level == 0:
            children.extend(childs)
        else:
            for c in childs:
                if safe(c): walk(c)
    walk(btree_addr)
    return children

# Read a Symbol Table Node → list of (name_offset, obj_header_addr)
def read_symtable_node(node_addr):
    assert sig(node_addr, 4) == b'SNOD', f"Expected SNOD at {node_addr:#x}"
    version  = u8(node_addr + 4)
    num_syms = u16(node_addr + 6)
    entries = []
    pos = node_addr + 8
    for i in range(num_syms):
        name_off    = u64(pos)
        obj_hdr_addr = u64(pos + 8)
        cache_type   = u32(pos + 16)
        # scratch pad 16 bytes
        entries.append((name_off, obj_hdr_addr, cache_type))
        pos += 40
    return entries

# List children of a group given its symbol table msg data
def list_group(btree_addr, heap_raw):
    leaf_children = read_btree_leaves(btree_addr)
    result = {}
    for c in leaf_children:
        if not safe(c): continue
        try:
            syms = read_symtable_node(c)
        except Exception as e:
            continue
        for name_off, oh_addr, cache_type in syms:
            if oh_addr == UNDEF or not safe(oh_addr): continue
            try:
                name = heap_name(heap_raw, name_off)
            except:
                name = f"<off={name_off}>"
            result[name] = (oh_addr, cache_type)
    return result

# Start from root group
root_oh_addr = 96
root_msgs = read_oh_v1(root_oh_addr)
print("Root OH messages:", [(t, s, l) for t,s,l in root_msgs])

# Find symbol table message (type 17)
for mtype, mstart, mlen in root_msgs:
    if mtype == 17:
        bt, hp = decode_symtable_msg(mstart)
        print(f"  Root group: btree={bt:#x}, heap={hp:#x}")
        heap_raw = read_local_heap(hp)
        root_children = list_group(bt, heap_raw)
        print("Root children:", list(root_children.keys()))
        break
