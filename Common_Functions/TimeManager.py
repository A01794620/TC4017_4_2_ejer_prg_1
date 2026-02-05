# List of Global Settings

# FileManager:
import time

class TimeManager:

    @staticmethod
    def get_time():
        return time.perf_counter()

    @staticmethod
    def get_execution_time(init, end):
        return end - init

    @staticmethod
    def get_utc():
        return time.time()