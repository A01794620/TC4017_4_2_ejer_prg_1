"""
 Module. String screen printer helper. Programming Individual Exercise: 4.2.1
 @Motive . Error Analysis using Pylint – PEP 8
 @author . Ronald Sandí Quesada
 @Student-ID . A01794620
 @email . A01794620@tec.mx
 @MNA Class . Pruebas de Software y Aseguramiento de la Calidad (TC4017)
 @Professor . PhD Gerardo Padilla Zárate
 @Professor Evaluator and Tutor . PhD Daniel Flores Araiza
 @Period . I Trimester 2026
 @Date
"""
# External Libraries
from colorama import init, Fore
init(autoreset=True)


class PrinterHelper:

    """
    String screen printer helper. It is a module who handles all related to screen printing.
    """

    @staticmethod
    def print_error(error_str):
        """
        Print messages under error or exception fashion.

        Args:
            error_str (string): Original error text to print.

        Returns:
           void: System print by console.
        """
        head_ = "==" * 40
        results_to_print = "\n" + head_ + "\n" + error_str + "\n" + head_ + "\n"
        print(f"{Fore.RED}The following errors were found in the system execution:"
              f"\n{results_to_print}")

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

        print(f"{Fore.RED}{results_to_print}")

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

    @staticmethod
    def print_time_stamp(execution_time, is_final_time_=True):
        """
        Print the execution time in the very last moment, after file is stored and
        results on screen. This elapsed time is wide bigger than the calculation time
        in the local machine.

            Args:
                execution_time (float): Execution time registered.
                is_final_time_ (bool): Flag to either display final time or execution time.
            Returns:
                void: System print by console.
        """


        if is_final_time_:
            print(f"{Fore.LIGHTWHITE_EX}Elapsed Time after saving file and listing on screen:"
                  f"{execution_time: .4f} seconds\n")
        else:
            print(f"{Fore.CYAN}Elapsed Execution Time:{execution_time: .4f} seconds\n")
