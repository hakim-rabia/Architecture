import re

# List of registers for reference
registers = ["$zero", "$at", "$v0", "$v1", "$a0", "$a1", "$a2", "$a3", "$t0", "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7", "$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", "$s7", "$t8", "$t9", "$k0", "$k1", "$gp", "$sp", "$fp", "$ra"]

# Dictionary to store label addresses
addresses = {}

def save_address(line, i):
    if line[0] == '@':
        addresses[line] = i

def get_address(line, i):
    if line == '@here':
        return i+2
    if line[:6] == '@here+':
        return i+int(line[6:])
    elif line in addresses:
        return addresses[line]
    else:
        return int(line)

def is_instruction(line):
    return line != '' and line[0] != '@'

def is_address(line):
    return len(line) > 1 and line[0] == '@'

def get_register(reg):
    if reg in registers:
        reg = registers.index(reg)
    else:
        reg = int(reg[1:])
    return "{0:05b}".format(reg)

def twos_complement(val, nbits):
    if val < 0:
        val = (1 << nbits) + val
    else:
        if (val & (1 << (nbits - 1))) != 0:
            val = val - (1 << nbits)
    return val

def int2word(val):
    if val < 0:
        val = (1 << 16) + val
    else:
        if (val & (1 << (16 - 1))) != 0:
            val = val - (1 << 16)
    return "{0:016b}".format(val)

def word2int(val_str):
    import sys
    val = int(val_str, 2)
    b = val.to_bytes(4, byteorder=sys.byteorder, signed=False)                                                          
    return str(int.from_bytes(b, byteorder=sys.byteorder, signed=False))
