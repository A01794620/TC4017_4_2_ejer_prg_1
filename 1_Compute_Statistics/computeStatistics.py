# Program 1 . Error Análysis using Pylint – PEP 8

# Requirements:
# Req1. The program shall be invoked from a command line. The program shall receive a file as parameter.
# The file will contain a list of items (presumable numbers).
# Req 2. The program shall compute all descriptive statistics from a file containing numbers.
# The results shall be print on a screen and on a file named StatisticsResults.txt.
# All computation MUST be calculated using the basic algorithms, not functions or libraries.
# The descriptive statistics are mean, median, mode, standard deviation, and variance.
# Req 3. The program shall include the mechanism to handle invalid data in the file.
# Errors should be displayed in the console and the execution must continue.
# Req 4. The name of the program shall be computeStatistics.py
# Req 5. The minimum format to invoke the program shall be as follows:
# python computeStatistics.py fileWithData.txt
# Req 6. The program shall manage files having from hundreds of items to thousands of items.
# Req 7. The program should include at the end of the execution the time elapsed for the execution and calculus of the
# data. This number shall be included in the results file and on the screen.
# Req 8. Be compliant with PEP8.


import time
import errno

RESOURCE_PATH = "P1\\"
ZERO_WHEN_NULL = 0.0

def standard_deviation(number_list_):
    variance_ = variance(number_list_)
    standard_deviation_ = variance_ ** 0.5
    return standard_deviation_


def variance(number_list_):
    mean_ = mean(number_list_)
    #print(mean_)

    variance_sum = ZERO_WHEN_NULL

    for number in number_list_:
        variance_item = (number - mean_) ** 2
        variance_sum += variance_item

    variance_ = variance_sum / (len(number_list_) -1)
    return variance_

def mode(number_list_):
    mode_counter = {}

    for number in number_list_:
        if number in mode_counter:
            mode_counter[number] += 1
        else:
            mode_counter[number] = 1
    mode_counter_sorted = dict(sorted(mode_counter.items(), key=lambda item: item[1], reverse=True))

    mode_, mode_hits = (next(iter(mode_counter_sorted.items())))

    if mode_hits > 1:
        return mode_
    else:
        return "n/a"


def median(number_list_):
    median_ = ZERO_WHEN_NULL
    position_to_take = ZERO_WHEN_NULL

    median_list = number_list[:]
    median_list.sort()

    length = len(number_list_)
    #print(length)

    #print(length % 2)

    if length % 2 == 0:
        #print("par")
        position_to_take = int(length / 2) - 1
        #print(f"position_to_take := {position_to_take}")

        #print(median_list[position_to_take])
        #print(median_list[position_to_take + 1])
        median_ = (median_list[position_to_take] + median_list[position_to_take + 1]) / 2
    else:
        #print("impar")
        position_to_take = int((length + 1) / 2) - 1
        median_ = median_list[position_to_take]
        #print(position_to_take)
        median_ = median_list[position_to_take]
    return median_


def mean(number_list_):
    return sum(number_list_) / len(number_list_)


def file_lines_to_float(file_lines_):
    number_list_ = []
    for number_in_line in file_lines_:
        try:
            number_from_string = float(number_in_line)
            number_list_.append(number_from_string)
        except ValueError as e:
            print(f"Error: Unable to convert '{number_in_line}' to a float. Details: {e}")
            # number_list_.append(ZERO_WHEN_NULL)
    return number_list_


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

def print_results(number_list_):
    # original_length = len(file_lines)
    length = len(number_list_)
    head_ = "=-" * 20
    results_to_print = f"{head_}\n" \
                       f"Count: {length}\n" \
                       f"Mean: {mean(number_list_)}\n" \
                       f"Median: {median(number_list_)}\n" \
                       f"Mode: {mode(number_list_)}\n" \
                       f"Standard Deviation: {standard_deviation(number_list_)}\n" \
                       f"Variance: {variance(number_list_)}\n" \
                       f"{head_}\n"

    print(results_to_print)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_time = time.perf_counter()

    for i in range(1,8):
        print(f"TC{i}.txt")
        file_lines = read_from_file(f"{RESOURCE_PATH}TC{i}.txt")
        number_list = file_lines_to_float(file_lines)
        print_results(number_list)

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
