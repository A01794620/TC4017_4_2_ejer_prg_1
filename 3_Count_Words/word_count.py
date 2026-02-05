"""
Program #1. Compute Statistics.
"""
import sys
from pathlib import Path
import os

_parent_dir = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parent_dir))

import common_functions.PrinterHelper as PrintHelp # noqa pylint: disable=wrong-import-position, import-error
import common_functions.GlobalSettings as CommonFxs # noqa pylint: disable=wrong-import-position, import-error
import common_functions.FileManager as FileM # noqa pylint: disable=wrong-import-position, import-error
import common_functions.TimeManager as TimeM # noqa pylint: disable=wrong-import-position, import-error


# Class: Pruebas de Software y Aseguramiento de la Calidad (TC4017)
# Programming Individual Exercise: 4.2.1 - Error Analysis using Pylint – PEP 8
# Professor: PhD Gerardo Padilla Zárate
# Tutor/Evaluator Professor: PhD Daniel Flores Araiza
# Student / Investigator: Ronald Sandí Quesada – (A01794620)
# I Trimester – 2026
# Date: 01/02/2026

#Requirements:
# Req 1.



# RESOURCE_PATH = "P3\\"

def count_words(file_lines_):
    """
    Count the words frequency from lines, which came from a file.

    Args:
        file_lines_ (string[]) : Set of Lines with Words to be counted.

    Returns:
        Tuple: Length of the unique frequency and the Words lines and counts.
    """

    word_counter = {}
    word_counter_text = ""

    for file_line in file_lines_:
        if file_line in word_counter:
            word_counter[file_line] += 1
        else:
            word_counter[file_line] = 1

    word_counter_sorted = dict(sorted(word_counter.items(), key=lambda item: item[1], reverse=True))

    for key, value in word_counter_sorted.items():
        word_counter_text = word_counter_text + f"{key}: {value}\n"

    return len(word_counter_sorted), word_counter_text


def print_results(exercise_id_, len_word_counter, word_counter_text, init_time_, disk_safe=True):
    """
    Print the computations results.

    Args:
        exercise_id_ (int) : Exercise ID.
        len_word_counter (int): Length of Word Counter.
        word_counter_text (float[]): The source list of words to be used as
        the print raw material.
        init_time_ (float): Initial registered time.
        disk_safe (bool): Flag to either save or not the results in the local disk.

    Returns:
        void: System print by console.
    """
    execution_time = TimeM.TimeManager.get_execution_time(init_time_, TimeM.TimeManager.get_time())

    results_to_print = (word_counter_text +
                        "\n" +
                        "Grand Total:\t" +  str(len_word_counter) + "\n" +
                        "Elapsed Execution Time:\t" +  str(execution_time) + "\n")

    PrintHelp.PrinterHelper.print_results(results_to_print)

    if disk_safe:
        FileM.FileManager.write_to_file(exercise_id_, results_to_print)

# Main Execution Point
if __name__ == '__main__':
    EXERCISE_ID = 3
    init_time = TimeM.TimeManager.get_time()

    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            print("Only the first argument is required. Extra arguments will be ignored.")

        file_to_proces = sys.argv[1]
        file_lines = FileM.FileManager.read_from_file(f"{CommonFxs.GlobalSettings.RESOURCE_PATH}"
                                                      f"{EXERCISE_ID}\\{file_to_proces}")

        #print(file_lines)
        len_word_counter_ , word_counter_text_ = count_words(file_lines)

        if len_word_counter_ >= 1:
            print_results(EXERCISE_ID, len_word_counter_, word_counter_text_, init_time, True)
    else:
        PrintHelp.PrinterHelper.print_help(os.path.abspath(__file__))
