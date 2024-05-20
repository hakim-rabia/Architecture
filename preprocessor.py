import re
from utils import is_instruction, is_address, save_address

def preprocess(lines):
    result = []
    for line in lines:
        line = line.split(";")[0]
        line = line.strip()
        line = line.lower()
        line = re.sub(' +', ' ', line)

        # MOVE
        line = re.sub('move', 'add $0', line)

        # LOADI
        line = re.sub('loadi', 'addi $0', line)

        # JAL
        if line.startswith('jal'):
            result.append('addi $0 $ra @here+2')
            line = 'j' + line[3:]
        
        # INC and DEC
        line = re.sub(
            r'inc (\$[a-zA-Z0-9_]+)', 
            lambda x: 'addi {} {} 1'.format(
                x.groups()[0],
                x.groups()[0],
            ), 
            line
        )
        line = re.sub(
            r'dec (\$[a-zA-Z0-9_]+)', 
            lambda x: 'addi {} {} -1'.format(
                x.groups()[0],
                x.groups()[0],
            ), 
            line
        )

        result.append(line)
    return result    
