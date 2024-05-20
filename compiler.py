from utils import get_register, get_address, int2word, twos_complement

opcodes = {
    "add":  0,
    "sub":  0,
    "mult": 0,
    "div":  0,
    "mod":  0,
    "and":  0,
    "or":   0,
    "slt":  0,
    "addi":  16,
    "subi":  17,
    "multi": 18,
    "divi":  19,
    "modi":  20,
    "andi":  21,
    "ori":   22,
    "slti":  23,
    "lw":   35,
    "sw":   43,
    "beq":  4,
    "j":    2,
    "jr":    8,
    "hlt": 63,
}

funct = {
    "add":  0,
    "sub":  1,
    "mult": 2,
    "div":  3,
    "mod":  4,
    "and":  5,
    "or":   6,
    "slt":  7,
}

def compile_line(code, i):
    instruction, *items = code.split(' ')

    binary = ''
    opcode = opcodes[instruction]
    if opcode == 0:  # R-Type
        binary += get_register(items[0])
        binary += get_register(items[1])
        binary += get_register(items[2])
        binary += "0" * 5
        binary += "{0:06b}".format(funct[instruction])
    elif opcode in [35, 43, 4] + list(range(16, 24)):  # Load / Store / Branch / I-Type
        binary += get_register(items[0])
        binary += get_register(items[1])
        if opcode == 4:
            binary += int2word(get_address(items[2], i) - (i + 1))
        else:
            binary += int2word(get_address(items[2], i))  # Get address will return integer if argument isn't an address
    elif opcode == 2:  # Jump
        binary += "{0:026b}".format(get_address(items[0], i))
    elif opcode == 8:  # Jump register
        binary += get_register(items[0])
        binary += "0" * 21
    else:
        binary = "0" * 26
    
    return "{0:06b}".format(opcode) + binary
