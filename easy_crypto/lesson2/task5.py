'''
# TASK 5 - write a function to generate all the possible shifts of an array of bytes
'''
from .task3 import shift_byte_array


def get_all_shifts(byte_array):
    ''' return all possible shifts of input byte array'''
    return [shift_byte_array(byte_array, shift) for shift in range(1, 256)]
