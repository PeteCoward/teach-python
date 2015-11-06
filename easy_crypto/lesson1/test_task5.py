from .task5 import get_shifted_string


def test_get_shifted_string():
    ''' get_shifted_string should correctly shift strings '''

    assert get_shifted_string('ABC', 1) == 'BCD'
    assert get_shifted_string('A C', 10) == 'K M'
