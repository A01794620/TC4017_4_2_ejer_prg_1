"""
Program #1. Compute Statistics.
"""


class GlobalSettings:
    """
    Program #1. Compute Statistics.
    """

    def __str__(self):
        return self.__class__.__name__

    @property
    def version(self):
        """
        Read the context of a plain file.

        Args:
            file_path_ (strig): File path to be read.

        Returns:
            string[]: The content of the file in lines separation.
        """
        return self.VER

    VER = "1.0"
    WORD_LEN_DEFAULT = 32
    RESOURCE_PATH = "P"
    ZERO_WHEN_NULL = 0
    BIN_DIVIDER = 2
    HEXA_DIVIDER = 16
    NA = "n/a"
    RESULT_PATH = "RESULTS\\"
    OUTPUT_FILE = "StatisticsResults.txt"
