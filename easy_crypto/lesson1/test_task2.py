import pytest
from .task2 import get_alphabet_letter


def test_get_alphabet_letter_works():
    ''' get_alphabet_letter should return correct indices '''
    letter = get_alphabet_letter(0)
    assert letter == 'A', "letter at 0 should be A"
    letter = get_alphabet_letter(2)
    assert letter == 'C', "letter at 2 should be C"
    letter = get_alphabet_letter(25)
    assert letter == 'Z', "letter at 25 should be Z"


def test_get_alphabet_letter_index_greater_than_25():
    ''' get_alphabet_letter should return -1 for non letters '''
    letter = get_alphabet_letter(26)
    assert letter == 'A', "get_alphabet_letter should return A for index 26"
    index = get_alphabet_letter(28)
    assert index == 'C', "get_alphabet_letter should return C for index 28"


def test_get_alphabet_letter_notinteger_valueerror():
    ''' get_alphabet_letter should raise a ValueError if input is not an integer '''
    with pytest.raises(ValueError):
        get_alphabet_letter('ab'), "get_alphabet_letter should raise a ValueError if input is not an integer"
        get_alphabet_letter(1.2), "get_alphabet_letter should raise a ValueError if input is not an integer"
