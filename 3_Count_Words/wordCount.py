"""
 Program #3. Word Counting. Programming Individual Exercise: 4.2.1
 @Motive . Error Analysis using Pylint – PEP 8
 @author . Ronald Sandí Quesada
 @Student-ID . A01794620
 @email . A01794620@tec.mx
 @MNA Class . Pruebas de Software y Aseguramiento de la Calidad (TC4017)
 @Professor . PhD Gerardo Padilla Zárate
 @Professor Evaluator and Tutor . PhD Daniel Flores Araiza
 @Period . I Trimester 2026
 @Date . 01/02/2026
"""

# External Libraries
import sys
from pathlib import Path
import os
# Project Common Classes
_parent_dir = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parent_dir))

import Common_Functions.PrinterHelper as PrintHelp # noqa pylint: disable=wrong-import-position, import-error
import Common_Functions.GlobalSettings as CommonFxs # noqa pylint: disable=wrong-import-position, import-error
import Common_Functions.FileManager as FileM # noqa pylint: disable=wrong-import-position, import-error
import Common_Functions.TimeManager as TimeM # noqa pylint: disable=wrong-import-position, import-error


# Req 1. .The program shall be invoked from a command line.
#        . The program shall receive a file as parameter.
#        . The file will contain a words (presumable between spaces).
# Req 2. .The program shall identify all distinct words and the frequency of them
#        (how many times the word “X” appears in the file).
#        .The results shall be print on a screen and on a file named WordCountResults.txt.
#        .All computation MUST be calculated using the basic algorithms, not functions or libraries.
# Req 3. .The program shall include the mechanism to handle invalid data in the file.
#        .Errors should be displayed in the console and the execution must continue.
# Req 4. .The name of the program shall be wordCount.py
# Req 5. .The minimum format to invoke the program shall be as follows:
#        python wordCount.py fileWithData.txt
# Req 6. .The program shall manage files having from hundreds of items to thousands of items.
# Req 7. .The program should include at the end of the execution the time elapsed for the
#        execution and calculus of the data.
#        This number shall be included in the results file and on the screen.
# Req 8. .Be compliant with PEP8.


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

# pylint: disable=R0913, R0917
def print_results(exercise_id_, len_word_counter, word_counter_text, init_time_,
                  file_source_name_, disk_safe=True):
    """
    Print the computations results.

    Args:
        exercise_id_ (int) : Exercise ID.
        len_word_counter (int): Length of Word Counter.
        word_counter_text (float[]): The source list of words to be used as
        the print raw material.
        init_time_ (float): Initial registered time.
        file_source_name_ (string): Original file name reference.
        disk_safe (bool): Flag to either save or not the results in the local disk.

    Returns:
        void: System print by console.
    """
    execution_time = TimeM.TimeManager.get_execution_time(init_time_, TimeM.TimeManager.get_time())

    results_to_print = word_counter_text + "Grand Total:\t" +  str(len_word_counter)
    PrintHelp.PrinterHelper.print_results(results_to_print)
    PrintHelp.PrinterHelper.print_time_stamp(execution_time, False)

    if disk_safe:
        results_to_save = (results_to_print +
                           f"\nElapsed Execution Time: {execution_time:.4f} seconds")
        FileM.FileManager.write_to_file(exercise_id_, file_source_name_, results_to_save)

    final_time = TimeM.TimeManager.get_execution_time(init_time_, TimeM.TimeManager.get_time())
    PrintHelp.PrinterHelper.print_time_stamp(final_time)


# Main Execution Point
if __name__ == '__main__':
    EXERCISE_ID = 3
    init_time = TimeM.TimeManager.get_time()

    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            print("Only the first argument is required. Extra arguments will be ignored.")

        file_to_proces = sys.argv[1]
        file_lines = FileM.FileManager.read_from_file(
            f"{CommonFxs.GlobalSettings.RESOURCE_PATH}"
            f"{EXERCISE_ID}\\{file_to_proces}", EXERCISE_ID)

        len_word_counter_ , word_counter_text_ = count_words(file_lines)

        if len_word_counter_ >= 1:
            file_source_name = file_to_proces.replace(".", "_")
            print_results(EXERCISE_ID, len_word_counter_, word_counter_text_, init_time,
                          file_source_name, True)
    else:
        PrintHelp.PrinterHelper.print_help(os.path.abspath(__file__))
