import pytest
from .task1 import get_alphabet_index


def test_get_alphabet_index_works():
    ''' get_alphabet_index should return correct indices '''
    index = get_alphabet_index('A')
    assert index == 0, "index of A should be 0"
    index = get_alphabet_index('C')
    assert index == 2, "index of C should be 2"
    index = get_alphabet_index('Z')
    assert index == 25, "index of Z should be 25"


def test_get_alphabet_index_accepts_lowercase():
    ''' get_alphabet_index should convert lowercase to uppercase '''
    index = get_alphabet_index('a')
    assert index == 0, "index of a should be 0"
    index = get_alphabet_index('c')
    assert index == 2, "index of c should be 2"
    index = get_alphabet_index('z')
    assert index == 25, "index of z should be 25"


def test_get_alphabet_index_notletter_returns_minus1():
    ''' get_alphabet_index should return -1 for non letters '''
    index = get_alphabet_index(' ')
    assert index == -1, "get_alphabet_index should return -1 for non letters"
    index = get_alphabet_index('%')
    assert index == -1, "get_alphabet_index should return -1 for non letters"


def test_get_alphabet_index_toolong_valueerror():
    ''' get_alphabet_index should raise a ValueError if input is not only 1 letter '''
    with pytest.raises(ValueError):
        get_alphabet_index('ab'), "get_alphabet_index should raise a ValueError if input is not only 1 letter"
        get_alphabet_index(''), "get_alphabet_index should raise a ValueError if input is not only 1 letter"


def test_get_alphabet_index_notstring_valueerror():
    ''' get_alphabet_index should raise a ValueError if input is not a string'''
    with pytest.raises(ValueError):
        get_alphabet_index(22), "get_alphabet_index should raise a ValueError if input is not a string"
        get_alphabet_index(4.5), "get_alphabet_index should raise a ValueError if input is not a string"
