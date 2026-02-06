"""
 Module. Time Manager. Programming Individual Exercise: 4.2.1
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
import time

class TimeManager:
    """
    Time Manager. It is a module who handles all processes related to Time manipulation.
    """

    @staticmethod
    def get_time():
        """
        Get the current system time.

        Args:
            no arguments.

        Returns:
            float: System time in numerical representation.
        """
        return time.perf_counter()

    @staticmethod
    def get_execution_time(init, end):
        """
        Calculates the elapsed time between the init and end times.

        Args:
            no arguments.

        Returns:
            float: The elapsed time calculation result.
        """
        return end-init

    @staticmethod
    def get_utc():
        """
        Returns the UTC time in numerical representation
        (seconds elapsed from <1-1-1970> until now).

        Args:
            no arguments.

        Returns:
            float: System UTC in seconds.
        """
        return time.time()
