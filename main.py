import os
import shutil
import time
from utils import *
from preprocessor import *
from compiler import *
from plotter import *

def main():
    src_path = './src/'
    bin_path = './binary/'
    dec_path = './decimal/'

    shutil.rmtree(bin_path, ignore_errors=True)
    shutil.rmtree(dec_path, ignore_errors=True)
    os.makedirs(bin_path)
    os.makedirs(dec_path)

    compile_times = []
    file_names = []

    for filename in os.listdir(src_path):
        start_time = time.time()  # Start timing

        file, ext = filename.split('.')
        binary = decimal = ''
        with open(src_path + filename) as f:
            lines = preprocess(f.readlines())
            lines = [l for l in lines if l != '']

            i = 0
            for line in lines:
                if is_instruction(line):
                    i += 1
                elif is_address(line):
                    save_address(line, i)

            lines = [l for l in lines if is_instruction(l)]

            for i, line in enumerate(lines):
                bin = compile_line(line, i)
                if not bin:
                    continue

                binary += bin + '\n'
                decimal += word2int(bin) + '\n'

        with open(bin_path + file + '.txt', 'w+') as f:
            f.write(binary)

        with open(dec_path + file + '.txt', 'w+') as f:
            f.write(decimal)

        end_time = time.time()  # End timing
        compile_times.append(end_time - start_time)
        file_names.append(filename)

        print(f'{filename} compiled in {end_time - start_time} seconds')

    plot_compilation_times(file_names, compile_times)

if __name__ == '__main__':
    main()
