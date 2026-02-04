# Program 2. Error Análysis using Pylint – PEP 8

# Requirements:

import time
import errno

WORD_LEN_DEFAULT = 32
RESOURCE_PATH = "P2\\"
ZERO_WHEN_NULL = 0
BIN_DIVIDER = 2
HEXA_DIVIDER = 16

def decimal_int_to_hexa(decimal_number, word_length=WORD_LEN_DEFAULT, pad_leading_zeros=False):
    hexa_carrier = []
    decimal_number_ = decimal_number

    if word_length <= ZERO_WHEN_NULL or word_length % 4 != ZERO_WHEN_NULL:
        raise ValueError("World System must be a Positive value and multiple of 4 (8, 16, 32, inter alia)")

    hexa_alfabet = {
                    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9',10: 'A', 11: 'B', 12: 'C', 13: 'D',14: 'E', 15: 'F'
    }

    if decimal_number_ == ZERO_WHEN_NULL:
        hexa_carrier = "0" * (word_length // 4)
        return hexa_carrier

    if decimal_number_ < ZERO_WHEN_NULL:
        decimal_number_ = (1 << word_length) + decimal_number

    while decimal_number_ > 0:
        remainder = decimal_number_ % HEXA_DIVIDER
        hexa_carrier.append(hexa_alfabet[remainder])
        decimal_number_ = decimal_number_ // HEXA_DIVIDER

    hexa_carrier_reverse = hexa_carrier[::-1]

    if pad_leading_zeros:
        while len(hexa_carrier_reverse) < word_length // 4:
            hexa_carrier_reverse.insert(0, '0')

    hexa_carrier_reverse = ''.join(hexa_carrier_reverse)

    return hexa_carrier_reverse

# Convert decimal to binary using pure mathematical operations.
# Supports negative numbers using two's complement.

def decimal_int_to_binary(dec_int_number, word_length=WORD_LEN_DEFAULT, pad_leading_zeros=False):
    bit_carrier = []
    dec_int_number_ = dec_int_number

    if word_length <= 0:
        raise ValueError("World System must be a Positive value (8, 16, 32, inter alia)")

    if dec_int_number_ == ZERO_WHEN_NULL:
        bit_carrier = "0" * word_length
        return bit_carrier

    if dec_int_number_ < ZERO_WHEN_NULL:
        dec_int_number_ = (1 << word_length) + dec_int_number

    while dec_int_number_ > 0:
        mod_ = dec_int_number_ % BIN_DIVIDER

        if mod_ == 0:
            bit_carrier.append("0")
        else:
            bit_carrier.append("1")

        dec_int_number_ = dec_int_number_ // BIN_DIVIDER

    bit_carrier_reverse = bit_carrier[::-1]

    if pad_leading_zeros:
        while len(bit_carrier_reverse) < word_length:
            bit_carrier_reverse.insert(0, '0')

    bit_carrier_reverse = ''.join(bit_carrier_reverse)
    return bit_carrier_reverse


def file_lines_to_binary(file_lines_):
    number_list_ = []
    for number_in_line in file_lines_:
        print(number_in_line)

        #try:
        #    number_from_string = float(number_in_line)
        #    number_list_.append(number_from_string)
        # except ValueError as e:
        #     print(f"Error: Unable to convert '{number_in_line}' to a float. Details: {e}")
        # number_list_.append(ZERO_WHEN_NULL)
    return number_list_

def read_from_file(file_path):
    source_file_lines = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                source_file_lines.append(line.strip())
        return source_file_lines
    except EnvironmentError as err:
        if err.errno == errno.ENOENT:
            print(
                f"File not found Exception when trying to load the file '{file_path}'.\nDouble Check the file path and try again.")
        else:
            print(
                f"There is a system problem to read the file '{file_path}'.\nDouble Check the file path and try again.")
        return source_file_lines
    except Exception as e:
        print(f"An error occurred: {e}")
        return source_file_lines

def file_lines_to_decimal_int(file_lines_):
    number_list_ = []
    for number_in_line in file_lines_:
        try:
            number_from_string = int(number_in_line)
            number_list_.append(number_from_string)
        except ValueError as e:
            print(f"Error: Unable to convert '{number_in_line}' to a decimal integer. Details: {e}")
            # number_list_.append(ZERO_WHEN_NULL)
    return number_list_

def print_results(dec_int_number_):
    # head_ = "=-" * 20
    bin_representation = decimal_int_to_binary(dec_int_number_)
    hexa_representation = decimal_int_to_hexa(dec_int_number_)

    results_to_print = f"> Decimal: {dec_int_number_}\t" \
                       f"Binary: {bin_representation}\t" \
                       f"Hexadecimal: {hexa_representation}"

    print(results_to_print)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers_container = []
    start_time = time.perf_counter()
    file_lines = read_from_file(f"{RESOURCE_PATH}TC4.txt")
    number_list = file_lines_to_decimal_int(file_lines)

    for dec_int_number_item in number_list:
        print_results(dec_int_number_item)

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
