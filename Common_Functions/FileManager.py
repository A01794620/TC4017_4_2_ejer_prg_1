"""
 Module. File Manager. Programming Individual Exercise: 4.2.1
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
import errno
from pathlib import Path
from colorama import init, Fore
init(autoreset=True)

# Project Common Classes
from Common_Functions.GlobalSettings import GlobalSettings # noqa pylint: disable=wrong-import-position, import-error
from Common_Functions.TimeManager import TimeManager # noqa pylint: disable=wrong-import-position, import-error
from Common_Functions.PrinterHelper import PrinterHelper # noqa pylint: disable=wrong-import-position, import-error

class FileManager:
    """
    File Manager. It is a module who handles all processes related to file manipulation.
    """

    @staticmethod
    def read_from_file(file_path_, exercise_id_):
        """
        Read the context of a plain file.

        Args:
            file_path_ (strig): File path to be read.
            exercise_id_ (int): The exercise ID as reference for the path file.

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
            error_to_print = ("Remember that the file might be located in the following"
                              " path to be read by the program:\n"
                              "\n~[Execution-Program-Directory]/" + GlobalSettings.RESOURCE_PATH +
                              str(exercise_id_) + "/[...] <--\n\n")

            if err.errno == errno.ENOENT:
                error_to_print = error_to_print + ("File not found Exception when trying to "
                                                   "load the file: '" +
                                  file_path_ + "'.\nDouble Check the file path and try again.")
            else:
                error_to_print = error_to_print + ("There is a system problem to read the file:'" +
                                  file_path_ + "'\nDouble Check the file path and try again.")

            PrinterHelper.print_error(error_to_print)

            return source_file_lines

    @staticmethod
    def write_to_file(exercise_id_, file_source_name, results_to_print_):
        """
        Writes data in a specific file in the local system.

            Args:
                exercise_id_ (int): The exersice ID as reference in the new path creation.
                file_source_name (string): Original file name reference.
                results_to_print_ (string): text to be saved in the file of the local system.

            Returns:
                void (void): Write the data in the file with no return.
        """
        head_ = "==" * 40
        results_to_print = head_ + "\n" + results_to_print_ + "\n" + head_ + "\n"

        try:
            file_path_to_write = FileManager.get_next_file_name_path(exercise_id_, file_source_name)
            file_path_to_write.parent.mkdir(parents=True, exist_ok=True)
            file_path_to_write.write_text(results_to_print, encoding="utf-8")
            print("Results stored in:")
            print(f"{Fore.CYAN}'{file_path_to_write}'")

        except FileNotFoundError as e:
            error_to_print = f"FileNotFoundError: {e}"
            PrinterHelper.print_error(error_to_print)

    @staticmethod
    def get_next_file_name_path(exercise_id_, file_source_name):
        """
        Calculates the next valid file path to be saved.

            Args:
                exercise_id_ (int): The exersice ID as reference in the new path creation.

            Returns:
                next valid path (string): It is a new folder/file to be created on the local system.
        """
        file_name_to_write = GlobalSettings.OUTPUT_FILE

        if exercise_id_ == 2:
            file_name_to_write = GlobalSettings.OUTPUT_FILE_CONVERSION
        elif exercise_id_ == 3:
            file_name_to_write = GlobalSettings.OUTPUT_FILE_WORD_COUNT

        current_utc_seconds = TimeManager.get_utc()
        current_utc_seconds = str(current_utc_seconds).replace(".", "_")
        plain_filename = (GlobalSettings.RESULT_PATH + GlobalSettings.RESOURCE_PATH +
                          str(exercise_id_) + "\\" + file_source_name + "\\" +
                          current_utc_seconds + "\\" +
                          file_name_to_write)

        return Path(plain_filename)
