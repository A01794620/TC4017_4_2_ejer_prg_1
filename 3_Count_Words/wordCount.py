# Program 2. Error Análysis using Pylint – PEP 8

# Requirements:

import time
import errno

RESOURCE_PATH = "P3\\"

def count_words(file_lines_):
    word_counter = {}

    for file_line in file_lines_:
        if file_line in word_counter:
            word_counter[file_line] += 1
        else:
            word_counter[file_line] = 1
        #print(file_line)

    word_counter_sorted = dict(sorted(word_counter.items(), key=lambda item: item[1], reverse=True))

    for key, value in word_counter_sorted.items():
        print(f"The word {key}: is {value} times.")

    #print(word_counter_sorted)

def read_from_file(file_path):
    source_file_lines = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                source_file_lines.append(line.strip())
        return source_file_lines
    except EnvironmentError as err:
        if err.errno == errno.ENOENT:
            print(
                f"File not found Exception when trying to load the file '{file_path}'.\nDouble Check the file path and try again.")
        else:
            print(
                f"There is a system problem to read the file '{file_path}'.\nDouble Check the file path and try again.")
        return source_file_lines
    except Exception as e:
        print(f"An error occurred: {e}")
        return source_file_lines


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    start_time = time.perf_counter()
    file_lines = read_from_file(f"{RESOURCE_PATH}TC5.txt")
    #print(file_lines)

    count_words(file_lines)

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")