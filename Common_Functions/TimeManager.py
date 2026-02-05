"""
Program #1. Compute Statistics.
"""

import time

class TimeManager:
    """
    Program #1. Compute Statistics.
    """

    @staticmethod
    def get_time():
        """
        Print help instructions to help the user on the right program usage.

        Args:
            no arguments.

        Returns:
            void: System print by console.
        """
        return time.perf_counter()

    @staticmethod
    def get_execution_time(init, end):
        """
        Print help instructions to help the user on the right program usage.

        Args:
            no arguments.

        Returns:
            void: System print by console.
        """
        return end - init

    @staticmethod
    def get_utc():
        """
        Print help instructions to help the user on the right program usage.

        Args:
            no arguments.

        Returns:
            void: System print by console.
        """
        return time.time()
