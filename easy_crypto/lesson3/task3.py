
## TASK 3 - compare a byte frequncy dictionary with the expected byte frequencies to give a numner
from .task1 import expected_byte_frequencies


def get_difference_rating(byte_frequencies):
    rating = 0
    for byte_value, expected_frequency in expected_byte_frequencies.items():
        actual_frequency = byte_frequencies.get(byte_value, 0)
        rating += abs(expected_frequency - actual_frequency)

    return rating
