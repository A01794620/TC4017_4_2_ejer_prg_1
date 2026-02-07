"""
 Program #1. Compute Statistics. Programming Individual Exercise: 4.2.1
 @Motive . Error Analysis using Pylint – PEP 8
 @author . Ronald Sandí Quesada
 @Student-ID . A01794620
 @email . A01794620@tec.mx
 @MNA Class . Pruebas de Software y Aseguramiento de la Calidad (TC4017)
 @Professor . PhD Gerardo Padilla Zárate
 @Professor Evaluator and Tutor . PhD Daniel Flores Araiza
 @Period . I Trimester 2026
 @Date . 01/02/2026
 @References: All the algorithm were methodologically based on the material of
              Bruce, Bruce & Gedeck (2022, pp. 8-15).
 @APA:  - Bruce, P., Bruce, A. & Gedeck, P. (2022). Estadística Práctica para
        Ciencia de Datos con R y Python. (2nd. ed.) (F. Martínez, Trans.). Marcombo.
"""

# External Libraries
import os
import sys
import math
from pathlib import Path
# Project Common Classes
_parent_dir = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parent_dir))

import Common_Functions.PrinterHelper as PrintHelp # noqa pylint: disable=wrong-import-position, import-error
import Common_Functions.GlobalSettings as CommonFxs # noqa pylint: disable=wrong-import-position, import-error

import Common_Functions.TimeManager as TimeM # noqa pylint: disable=wrong-import-position, import-error
import Common_Functions.FileManager as FileM # noqa pylint: disable=wrong-import-position, import-error

# Requirements:
# Req 1. . The program shall be invoked from a command line.
#        . The program shall receive a file as parameter.
#        . The file will contain a list of items (presumable numbers).
# Req 2. . The program shall compute all descriptive statistics from a file containing numbers.
#        . The results shall be print on a screen and on a file named StatisticsResults.txt.
#        . All computation MUST be calculated using the basic algorithms, not functions or
#          libraries.
#        . The descriptive statistics are mean, median, mode, standard deviation, and variance.
# Req 3. . The program shall include the mechanism to handle invalid data in the file.
#        . Errors should be displayed in the console and the execution must continue.
# Req 4. . The name of the program shall be computeStatistics.py
# Req 5. . The minimum format to invoke the program shall be as follows:
#        . python computeStatistics.py fileWithData.txt
# Req 6. . The program shall manage files having from hundreds of items to thousands of items.
# Req 7. . The program should include at the end of the execution the time elapsed
#          for the execution and calculus of the data. This number shall be included in the
#          results file and on the screen.
# Req 8. . Be compliant with PEP8.

def standard_deviation(number_list_):
    """
    Calculates the Standard Deviation (SD) of a list of numbers.

    Args:
        number_list_ (float[]): The source list of numbers to be used as
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
        mode_ = CommonFxs.GlobalSettings.NA

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

    median_list = []

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

    for number in number_list_:
        if not math.isnan(number):
            sum_ = sum_ + number

    mean_ = sum_ / len(number_list_)
    return mean_


def file_lines_to_float(file_lines_, include_nil_counts=True):
    """
    Convert a String List to Float Point List.
    The non-numeric values are not converted.
    The flag included_nil_counts define either or not to include the N/A item in the list.

    Args:
        file_lines_ (Sting[]): The source list of lines in the file as String List.
        include_nil_counts (Boolean): Flag that defines either to include or not the N/A
        items in the list.

    Returns:
        float (Float[]): Numbers converted as a List.
    """
    number_list_ = []
    error_tracker = ""

    for number_in_line in file_lines_:
        try:
            number_from_string = float(number_in_line)
            number_list_.append(number_from_string)
        except ValueError as e:
            error_tracker = error_tracker + "× Error: Unable to convert '" + \
                            str(number_in_line) + "' to a float. Details: " + \
                            str(e) + "\n"

            if include_nil_counts:
                number_list_.append(float('nan'))

    if len(error_tracker) > 0:
        PrintHelp.PrinterHelper.print_error(error_tracker)

    return number_list_


def print_results(exercise_id_, number_list_, init_time_, file_source_name_, disk_safe=True):
    """
    Print the computations results.

    Args:
        exercise_id_ (int) : Exercise ID.
        number_list_ (float[]): The source list of numbers to be used as
                                the print raw material.
        init_time_ (float): Initial registered time.
        file_source_name_ (string): Original file name reference.
        disk_safe (bool): Flag to either save or not the results in the local disk.

    Returns:
        void: System print by console.
    """
    length = len(number_list_)

    execution_time = TimeM.TimeManager.get_execution_time(init_time_, TimeM.TimeManager.get_time())

    results_to_print = f"Count: {length}\n" \
                       f"Mean: {mean(number_list_)}\n" \
                       f"Median: {median(number_list_)}\n" \
                       f"Mode: {mode(number_list_)}\n" \
                       f"SD: {standard_deviation(number_list_)}\n" \
                       f"Variance: {variance(number_list_)}"

    if disk_safe:
        results_to_save = (results_to_print +
                           f"\nElapsed Execution Time: {execution_time:.4f} seconds")
        FileM.FileManager.write_to_file(exercise_id_,file_source_name_, results_to_save)

    PrintHelp.PrinterHelper.print_results(results_to_print)
    PrintHelp.PrinterHelper.print_time_stamp(execution_time, False)
    final_time = TimeM.TimeManager.get_execution_time(init_time_, TimeM.TimeManager.get_time())
    PrintHelp.PrinterHelper.print_time_stamp(final_time)

# Main Execution Point
if __name__ == '__main__':
    EXERCISE_ID = 1

    init_time = TimeM.TimeManager.get_time()

    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            print("Only the first argument is required. Extra arguments will be ignored.")

        file_to_proces = sys.argv[1]

        file_lines = FileM.FileManager.read_from_file(
            f"{CommonFxs.GlobalSettings.RESOURCE_PATH}{EXERCISE_ID}\\{file_to_proces}",
            EXERCISE_ID)

        number_list = file_lines_to_float(file_lines, True)

        if len(number_list)>=1:
            file_source_name = file_to_proces.replace(".", "_")
            print_results(EXERCISE_ID, number_list, init_time, file_source_name, True)
    else:
        PrintHelp.PrinterHelper.print_help(os.path.abspath(__file__))
