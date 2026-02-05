# List of Global Settings

# FileManager:
import errno
from pathlib import Path

from Common_Functions.GlobalSettings import GlobalSettings
from Common_Functions.TimeManager import TimeManager


class FileManager:

    @staticmethod
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

    @staticmethod
    def write_to_file(exercise_id_, results_to_print_):
        head_ = "=-" * 20
        results_to_print = (head_ + "\n" + results_to_print_ + head_ + "\n")

        try:
            file_path_to_write = FileManager.get_next_file_name_path(exercise_id_)
            file_path_to_write.parent.mkdir(parents=True, exist_ok=True)
            file_path_to_write.write_text(results_to_print)
            print(f"Results storage in '{file_path_to_write}'")
        except FileNotFoundError as e:
            print(f"FileNotFoundError:\n{e}")

    @staticmethod
    def get_next_file_name_path(exercise_id_):
        """
        Calculates the next valid file path to be saved.

            Args:
                exercise_id_ (int): The exersice ID as reference in the new path creation.

            Returns:
                next valid path (string): It is a new folder/file to be created on the local system.
        """
        current_utc_seconds = TimeManager.get_utc()
        current_utc_seconds = str(current_utc_seconds).replace(".", "_")

        #plain_filename = Path(file_path_).stem

        plain_filename = GlobalSettings.RESULT_PATH + GlobalSettings.RESOURCE_PATH + str(exercise_id_) + "\\" + current_utc_seconds + "\\" + GlobalSettings.OUTPUT_FILE
        return Path(plain_filename)
