# List of Global Settings

# FileManager:

from Common_Functions.TimeManager import TimeManager
from Common_Functions.FileManager import FileManager

class PrinterHelper:

    @staticmethod
    def print_help(exec_id):
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
                           f"Invocation example:\n\tpython {exec_id} fileWithData.txt\n" \
                           f"{head_}\n"

        print(results_to_print)

    @staticmethod
    def print_results(results_to_print_):
        """
        Print the computations results.

        Args:

            results_to_print_ (string): Original text to print.
            disk_safe (bool): Flag to either save or not the results in the local disk.
            init_time_ (float): Initial registered time.

        Returns:
            void: System print by console.
        """

        head_ = "=-" * 20
        results_to_print = (head_ + "\n" + results_to_print_ + "\n" + head_ + "\n")
        print(results_to_print)
