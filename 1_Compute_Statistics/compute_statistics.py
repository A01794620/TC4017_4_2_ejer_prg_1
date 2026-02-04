"""
Program #1. Compute Statistics.
"""
import os
import sys
import math
import time
import errno
from pathlib import Path

# Class: Pruebas de Software y Aseguramiento de la Calidad (TC4017)
# Programming Individual Exercise: 4.2.1 - Error Analysis using Pylint – PEP 8
# Professor: PhD Gerardo Padilla Zárate
# Tutor/Evaluator Professor: PhD Daniel Flores Araiza
# Student / Investigator: Ronald Sandí Quesada – (A01794620)
# I Trimester – 2026
# Date: 01/02/2026


#Requirements:
# Req 1. The program shall be invoked from a command line.
#        The program shall receive a file as parameter.
#        The file will contain a list of items (presumable numbers).
# Req 2. The program shall compute all descriptive statistics from a file containing numbers.
#        The results shall be print on a screen and on a file named StatisticsResults.txt.
#        All computation MUST be calculated using the basic algorithms, not functions or libraries.
#        The descriptive statistics are mean, median, mode, standard deviation, and variance.
# Req 3. The program shall include the mechanism to handle invalid data in the file.
#        Errors should be displayed in the console and the execution must continue.
# Req 4. The name of the program shall be compute_statistics.py
# Req 5. The minimum format to invoke the program shall be as follows:
#        python compute_statistics.py fileWithData.txt
# Req 6. The program shall manage files having from hundreds of items to thousands of items.
# Req 7. The program should include at the end of the execution the time elapsed
#        for the execution and calculus of the data. This number shall be included in the
#        results file and on the screen.
# Req 8. Be compliant with PEP8.


NA = "n/a"
ZERO_WHEN_NULL = 0.0
RESOURCE_PATH = "P1\\"
RESULT_PATH = "RESULTS\\"
OUTPUT_FILE = "StatisticsResults.txt"

def get_next_file_name_path(file_path_):
    """
    Calculates the next valid file path to be saved.

    Args:
        file_path_ (string): The original file path to be used a reference in the
        new path creation.
,
    Returns:
        next valid path (string): It is a new folder/file to be created on the local system.
    """

    current_utc_seconds = time.time()
    current_utc_seconds = str(current_utc_seconds).replace(".", "_")
    plain_filename = Path(file_path_).stem
    plain_filename = RESULT_PATH + plain_filename + "\\" + current_utc_seconds + "\\" + OUTPUT_FILE
    return Path(plain_filename)

def standard_deviation(number_list_):
    """
    Calculates the Standard Deviation (SD) of a list of numbers.

    Args:
        number_list_ (float): The source list of numbers to be used as
        the SD raw material.

    Returns:
        float: SD calculated.
    """
    variance_ = variance(number_list_)
    standard_deviation_ = variance_ ** 0.5
    return standard_deviation_


def variance(number_list_):
    """
    Calculates the variance of a list of numbers.

    Args:
        number_list_ (float[]): The source list of numbers to be used as
        the calculation raw material.

    Returns:
        float: calculated variance.
    """
    mean_ = mean(number_list_)
    variance_sum = 0.0

    for number in number_list_:
        if not math.isnan(number):
            variance_item = (number - mean_) ** 2
            variance_sum += variance_item

    variance_ = variance_sum / (len(number_list_) -1)
    return variance_

def mode(number_list_):
    """
    Calculates the Mode of a list of numbers.

    Args:
        number_list_ (float[]): The source list of numbers to be used as
        the calculation raw material.

    Returns:
        string: mode calculated.
    """
    mode_counter = {}

    for number in number_list_:
        if not math.isnan(number):
            if number in mode_counter:
                mode_counter[number] += 1
            else:
                mode_counter[number] = 1

    mode_counter_sorted = dict(sorted(mode_counter.items(), key=lambda item: item[1], reverse=True))
    mode_, mode_hits = (next(iter(mode_counter_sorted.items())))

    if mode_hits >=2:
        mode_ = str(mode_)
    else:
        mode_ = NA

    return mode_


def median(number_list_):
    """
    Calculates the Median of a list of numbers.

    Args:
        number_list_ (float[]): The source list of numbers to be used as
        the calculation raw material.

    Returns:
        float: Median calculated.
    """
    median_ = 0.0
    position_to_take = 0

    median_list = [] #number_list_[:]

    for number in number_list_:
        if not math.isnan(number):
            median_list.append(number)

    median_list.sort()

    length = len(median_list)

    if length % 2 == 0:
        # Even
        position_to_take = int(length / 2) - 1
        median_ = (median_list[position_to_take] + median_list[position_to_take + 1]) / 2
    else:
        # Odd
        position_to_take = int((length + 1) / 2) - 1
        median_ = median_list[position_to_take]

    return median_


def mean(number_list_):
    """
    Calculates the Mean of a list of numbers.

    Args:
        number_list_ (float[]): The source list of numbers to be used as
        the calculation raw material.

    Returns:
        float: Mean calculated.
    """
    sum_ = 0.0
    mean_= 0.0

    for number in number_list_:
        if not math.isnan(number):
            sum_ = sum_ + number

    mean_ = sum_ / len(number_list_)
    return mean_


def file_lines_to_float(file_lines_, include_nil_counts=True):
    """
    Convert a String List to Float Point List.
    The non-numeric values are not converted.
    The flag included_nil_counts define either or not to include the NA item in the list.

    Args:
        file_lines_ (Sting[]): The source list of lines in the file as String List.
        include_nil_counts (Boolean): Flag that defines either to include the NA item in the list.

    Returns:
        float (Float[]): Numbers converted as a List.
    """
    number_list_ = []
    for number_in_line in file_lines_:
        try:
            number_from_string = float(number_in_line)
            number_list_.append(number_from_string)
        except ValueError as e:
            print(f"Error: Unable to convert '{number_in_line}' to a float. Details: {e}")

            if include_nil_counts:
                number_list_.append(float('nan'))

    return number_list_


def read_from_file(file_path_):
    """
    Read the context of a plain file.

    Args:
        file_path_ (strig): File path to be read.

    Returns:
        string[]: The content of the file in lines separation.
    """
    source_file_lines = []

    try:
        with open(file_path_, 'r', encoding="utf-8") as file:
            for line in file:
                source_file_lines.append(line.strip())

        return source_file_lines
    except EnvironmentError as err:
        if err.errno == errno.ENOENT:
            print(
                f"File not found Exception when trying to load the file '{file_path_}'"
                ".\nDouble Check the file path and try again.")
        else:
            print(
                f"There is a system problem to read the file '{file_path_}'."
                "\nDouble Check the file path and try again.")
        return source_file_lines


def print_results(number_list_,file_path_, init_time_, disk_safe=True):
    """
    Print the computations results.

    Args:
        number_list_ (float[]): The source list of numbers to be used as
        the print raw material.
        file_path_ (string): Original source file location.
        disk_safe (bool): Flag to either save or not the results in the local disk.
        init_time_ (float): Initial registered time.

    Returns:
        void: System print by console.
    """

    length = len(number_list_)
    head_ = "=-" * 20
    execution_time = get_execution_time(init_time)

    results_to_print = f"{head_}\n" \
                       f"Count: {length}\n" \
                       f"Mean: {mean(number_list_)}\n" \
                       f"Median: {median(number_list_)}\n" \
                       f"Mode: {mode(number_list_)}\n" \
                       f"SD: {standard_deviation(number_list_)}\n" \
                       f"Variance: {variance(number_list_)}\n" \
                       f"Elapsed Execution Time: {execution_time} seconds\n" \
                       f"{head_}\n"

    if disk_safe:
        file_path_to_write = get_next_file_name_path(file_path_)
        file_path_to_write.parent.mkdir(parents=True, exist_ok=True)
        file_path_to_write.write_text(results_to_print)


        ##with open(file_path_to_write, 'w') as file:
        #    file_path_to_write.parent.mkdir(parents=True, exist_ok=True)
        #    file_path_to_write.write(results_to_print)
        #try:
        #    os.mkdir(file_path_to_write)
        #    print(f"Directory '{file_path_to_write}' created.")
        #except FileExistsError:
        #    print(f"Directory '{file_path_to_write}' already exists.")
        #except FileNotFoundError:
        #    print(f"Parent directory does not exist.")

        print(f"Results storage in '{file_path_to_write}'")

    print(results_to_print)

def print_help():
    """
    Print help instructions to help the user on the right program usage.

    Args:
        no arguments.

    Returns:
        void: System print by console.
    """
    head_ = "=-=" * 30
    results_to_print = f"{head_}\n" \
                       f"This program requires one parameter indicating the file to be " \
                       f"processed.\nAdditional parameters will be ignored.\n" \
                       f"Invocation example:\n\tpython compute_statistics.py fileWithData.txt\n" \
                       f"{head_}\n"

    print(results_to_print)

def get_time():
    return time.perf_counter()

def get_execution_time(init):
    return get_time() - init


# Main Execution Point
if __name__ == '__main__':
    init_time = get_time()

    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            print("Only the first argument is required. Extra arguments will be ignored.")
        file_to_proces = sys.argv[1]
        file_lines = read_from_file(f"{RESOURCE_PATH}{file_to_proces}")
        number_list = file_lines_to_float(file_lines, True)

        if len(number_list)>=1:
            print_results(number_list,f"{RESOURCE_PATH}{file_to_proces}", init_time, True)
        else:
            print_help()
