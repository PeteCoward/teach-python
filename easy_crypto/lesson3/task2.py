## TASK 2 - reutrn the percentages for each byte occurs in a byte array - hint search for 'Counter' in your documentation
from collections import Counter


def get_byte_frequencies(byte_array):
    counter = Counter(byte_array)
    frequencies = {}
    for byte_value, count in counter.items():
        frequencies[byte_value] = count * 100 / len(byte_array)
    return frequencies
