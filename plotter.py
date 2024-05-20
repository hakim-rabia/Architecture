import matplotlib.pyplot as plt

def plot_compilation_times(file_names, compile_times):
    plt.figure(figsize=(10, 5))
    plt.bar(file_names, compile_times, color='blue')
    plt.xlabel('File Names')
    plt.ylabel('Compilation Time (seconds)')
    plt.title('Compilation Time per File')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
