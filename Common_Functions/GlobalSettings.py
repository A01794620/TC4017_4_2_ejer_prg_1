"""
 Module. Global Settings Holder. Programming Individual Exercise: 4.2.1
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


class GlobalSettings:
    """
    Global Settings. A placeholder for global settings space.
    """

    def __str__(self):
        return self.__class__.__name__

    @property
    def version(self):
        """
        Package version.

        Args:
            (void): no arguments.

        Returns:
            ver (string): Package version.
        """
        return self.VER

    # GLobal settings to be used across all modules.
    VER = "1.0"
    WORD_LEN_DEFAULT = 32
    RESOURCE_PATH = "P"
    ZERO_WHEN_NULL = 0
    BIN_DIVIDER = 2
    HEXA_DIVIDER = 16
    NA = "n/a"
    RESULT_PATH = "RESULTS\\"
    OUTPUT_FILE = "StatisticsResults.txt"
    OUTPUT_FILE_CONVERSION = "ConvertionResults.txt"
    OUTPUT_FILE_WORD_COUNT = "WordCountResults.txt"
