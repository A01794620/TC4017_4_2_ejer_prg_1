import time
import sys

from pathlib import Path
_parent_dir = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parent_dir))
import Common_Functions.PrinterHelper as PrintHelp # noqa pylint: disable=wrong-import-position, import-error
import Common_Functions.GlobalSettings as CommonFxs # noqa pylint: disable=wrong-import-position, import-error
import Common_Functions.TimeManager as TimeM # noqa pylint: disable=wrong-import-position, import-error

# Main Execution Point
if __name__ == '__main__':
    init_ = TimeM.TimeManager.get_time()
    time.sleep(11)
    end_ = TimeM.TimeManager.get_time()
    elapsed_ = TimeM.TimeManager.get_execution_time(init_, end_)
    print(init_)
    print(end_)
    print(elapsed_)
    print(f"Elapsed time: {elapsed_:.4f} seconds")

