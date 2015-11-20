'''
# TASK 3 - write a function to shift an array of bytes by caesar shift
'''


def shift_byte_array(byte_array, shift):
    table = bytearray([(i + shift) % 256 for i in range(0, 256)])
    return byte_array.translate(table)
