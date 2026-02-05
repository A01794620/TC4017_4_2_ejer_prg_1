"""
Program #1. Compute Statistics.
"""
from colorama import init, Fore, Style
init(autoreset=True)

class PrinterHelper:

    """
    Program #1. Compute Statistics.
    """
    @staticmethod
    def print_error(error_str):
        """
        Print help instructions to help the user on the right program usage.

        Args:
            error_str (string): Original error text to print.

        Returns:
           void: System print by console.
        """
        head_ = "==" * 40
        results_to_print = "\n" + head_ + "\n" + error_str + "\n" + head_ + "\n"
        print(f"{Fore.RED}The following errors were found in the system execution:\n{error_str}")

    @staticmethod
    def print_help(exec_id):
        """
        Print help instructions to help the user on the right program usage.

        Args:
            no arguments.

        Returns:
            void: System print by console.
        """


        head_ = "==" * 40
        results_to_print = f"\n{head_}\n" \
                           f"This program requires one parameter indicating the file to be " \
                           f"processed.\nAdditional parameters will be ignored.\n" \
                           f"Invocation example:\n  python '{exec_id}' 'fileWithData.txt'\n" \
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

        head_ = "==" * 40
        results_to_print = head_ + "\n" + results_to_print_ + "\n" + head_ + "\n"
        print(results_to_print)
