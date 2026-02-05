"""
Program #3. Compute Statistics.
"""
# Requirements:

import sys
from pathlib import Path
import os
import math

_parent_dir = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parent_dir))

import common_functions.PrinterHelper as PrintHelp # noqa pylint: disable=wrong-import-position, import-error
import common_functions.GlobalSettings as CommonFxs # noqa pylint: disable=wrong-import-position, import-error
import common_functions.FileManager as FileM # noqa pylint: disable=wrong-import-position, import-error
import common_functions.TimeManager as TimeM # noqa pylint: disable=wrong-import-position, import-error


def decimal_int_to_hexa(
        decimal_number,
        word_length=CommonFxs.GlobalSettings.WORD_LEN_DEFAULT,
        pad_leading_zeros=False
):
    """
    Convert a String List to Decimal Integer.
    The non-numeric values are not converted.
    The flag included_nil_counts define either or not to include the NA item in the list.

    Args:
        decimal_number (float[]): The source list of decimal numbers to be converted to hexadecimal.
        word_length (int): The length of the World System to be converted.
        pad_leading_zeros (bool) Flag that defines either to include or not the padding 0's.

    Returns:
        hexadecimal float (float[]): Numbers converted as a List in hexadecimal format.
    """

    hexa_carrier = []
    decimal_number_ = decimal_number

    if (word_length <= CommonFxs.GlobalSettings.ZERO_WHEN_NULL or
            word_length % 4 != CommonFxs.GlobalSettings.ZERO_WHEN_NULL):
        raise ValueError("World System must be a Positive value and multiple of 4 "
                         "(8, 16, 32, inter alia)")

    hexa_alfabet = {
                    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9',10: 'A', 11: 'B', 12: 'C', 13: 'D',14: 'E', 15: 'F'
    }

    if decimal_number_ == CommonFxs.GlobalSettings.ZERO_WHEN_NULL:
        hexa_carrier = "0" * (word_length // 4)
        return hexa_carrier

    if decimal_number_ < CommonFxs.GlobalSettings.ZERO_WHEN_NULL:
        decimal_number_ = (1 << word_length) + decimal_number

    while decimal_number_ > 0:
        remainder = decimal_number_ % CommonFxs.GlobalSettings.HEXA_DIVIDER
        hexa_carrier.append(hexa_alfabet[remainder])
        decimal_number_ = decimal_number_ // CommonFxs.GlobalSettings.HEXA_DIVIDER

    hexa_carrier_reverse = hexa_carrier[::-1]

    if pad_leading_zeros:
        while len(hexa_carrier_reverse) < word_length // 4:
            hexa_carrier_reverse.insert(0, '0')

    hexa_carrier_reverse = ''.join(hexa_carrier_reverse)

    return hexa_carrier_reverse

# Convert decimal to binary using pure mathematical operations.
# Supports negative numbers using two's complement.

def decimal_int_to_binary(
        dec_int_number,
        word_length=CommonFxs.GlobalSettings.WORD_LEN_DEFAULT,
        pad_leading_zeros=False):

    """
        Convert a String List to Binary 'String'
        The non-numeric values are not converted.

        Args:
            dec_int_number (float[]): The source list of decimal numbers to be converted to binary.
            word_length (int): The length of the World System to be converted.
            pad_leading_zeros (bool) Flag that defines either to include or not the padding 0's.

        Returns:
            binary string (string[]): Numbers converted as a List in binary format.
        """


    bit_carrier = []
    dec_int_number_ = dec_int_number

    if word_length <= 0:
        raise ValueError("World System must be a Positive value (8, 16, 32, inter alia)")

    if dec_int_number_ == CommonFxs.GlobalSettings.ZERO_WHEN_NULL:
        bit_carrier = "0" * word_length
        return bit_carrier

    if dec_int_number_ < CommonFxs.GlobalSettings.ZERO_WHEN_NULL:
        dec_int_number_ = (1 << word_length) + dec_int_number

    while dec_int_number_ > 0:
        mod_ = dec_int_number_ % CommonFxs.GlobalSettings.BIN_DIVIDER

        if mod_ == 0:
            bit_carrier.append("0")
        else:
            bit_carrier.append("1")

        dec_int_number_ = dec_int_number_ // CommonFxs.GlobalSettings.BIN_DIVIDER

    bit_carrier_reverse = bit_carrier[::-1]

    if pad_leading_zeros:
        while len(bit_carrier_reverse) < word_length:
            bit_carrier_reverse.insert(0, '0')

    bit_carrier_reverse = ''.join(bit_carrier_reverse)
    return bit_carrier_reverse


def file_lines_to_decimal_int(file_lines_, include_nil_counts=True):
    """
    Convert a String List to Decimal Integer.
    The non-numeric values are not converted.
    The flag included_nil_counts define either or not to include the NA item in the list.

    Args:
        file_lines_ (Sting[]): The source list of lines in the file as String List.
        include_nil_counts (Boolean): Flag that defines either to include the NA item in the list.

    Returns:
        decimal integer (integer[]): Numbers converted as a List.
    """

    number_list_ = []
    for number_in_line in file_lines_:
        try:
            number_from_string = int(number_in_line)
            number_list_.append(number_from_string)
        except ValueError as e:
            print(f"Error: Unable to convert '{number_in_line}' to a decimal integer. Details: {e}")
            if include_nil_counts:
                number_list_.append(float('nan'))

    return number_list_


def print_results(exercise_id_, dec_int_number_, init_time_, disk_safe=True):
    """
    Print the computations results.

    Args:
        exercise_id_ (int) : Exercise ID.
        dec_int_number_ (float[]): The source list of numbers to be used as
        the print raw material.
        init_time_ (float): Initial registered time.
        disk_safe (bool): Flag to either save or not the results in the local disk.

    Returns:
        void: System print by console.
    """
    results_to_print = ""

    for item_id, dec_int_number_item_ in enumerate(dec_int_number_):
        line_to_print = ""

        if not math.isnan(dec_int_number_item_):
            bin_representation = decimal_int_to_binary(dec_int_number_item_)
            hexa_representation = decimal_int_to_hexa(dec_int_number_item_)
            line_to_print = (str(item_id) + "\t" + "Decimal:" + str(dec_int_number_item_) + "\t" +
                             "Hexadecimal:\t" + hexa_representation + "\t" + "Binary:\t" +
                             str(bin_representation) + "\n")
        else:
            line_to_print = str(item_id) + "\tDecimal:\tn/a\tHexadecimal:\t n/a\t\tBinary:\tn/a\n"

        results_to_print = results_to_print + line_to_print

    execution_time = TimeM.TimeManager.get_execution_time(init_time_, TimeM.TimeManager.get_time())

    results_to_print = results_to_print + "Elapsed Execution Time:\t" + str(execution_time) + "\n"

    PrintHelp.PrinterHelper.print_results(results_to_print)

    if disk_safe:
        FileM.FileManager.write_to_file(exercise_id_, results_to_print)


# Main Execution Point
if __name__ == '__main__':
    EXERCISE_ID = 2
    init_time = TimeM.TimeManager.get_time()

    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            print("Only the first argument is required. Extra arguments will be ignored.")

        file_to_proces = sys.argv[1]
        file_path_ = str(CommonFxs.GlobalSettings.RESOURCE_PATH) + "" + str(EXERCISE_ID) + "\\" + str(file_to_proces)
        file_lines = FileM.FileManager.read_from_file(file_path_)
        number_list = file_lines_to_decimal_int(file_lines)

        if len(number_list) >= 1:
            print_results(EXERCISE_ID, number_list, init_time, True)
    else:
        PrintHelp.PrinterHelper.print_help(os.path.abspath(__file__))
