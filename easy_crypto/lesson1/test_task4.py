from .task4 import get_shifted_letter


def test_get_shifted_letter():
    ''' get the shifted letter in the alphabet cycling from Z to A '''
    assert get_shifted_letter('A', 1) == 'B', "the next letter after A should be B"
    assert get_shifted_letter('M', 1) == 'N', "the next letter after M should be N"
    assert get_shifted_letter('Z', 1) == 'A', "the next letter after Z should be A"
    assert get_shifted_letter('A', 3) == 'D', "the third letter after A should be D"
    assert get_shifted_letter('M', 3) == 'P', "the third letter after M should be P"
    assert get_shifted_letter('Z', 3) == 'C', "the third letter after Z should be C"


def test_get_shifted_letter_does_not_change_nonletters():
    ''' get_shifted_letter should not change non letter characters '''
    assert get_shifted_letter(' ', 3) == ' ', "spaces should be unchanged"
