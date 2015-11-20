from .task3 import shift_byte_array


def test_get_next_letter():
    ''' get the next letter in the alphabet cycling from Z to A '''
    assert shift_byte_array(bytearray([0, 2, 5]), 1) == bytearray([1, 3, 6])
    assert shift_byte_array(bytearray([0, 2, 5]), 10) == bytearray([10, 12, 15])
    assert shift_byte_array(bytearray([250, 2, 5]), 10) == bytearray([4, 12, 15])
