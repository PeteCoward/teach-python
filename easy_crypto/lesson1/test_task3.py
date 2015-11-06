from .task3 import get_next_letter


def test_get_next_letter():
    ''' get the next letter in the alphabet cycling from Z to A '''
    assert get_next_letter('A') == 'B', "the next letter after A should be B"
    assert get_next_letter('M') == 'N', "the next letter after M should be N"
    assert get_next_letter('Z') == 'A', "the next letter after Z should be A"


def test_get_next_letter_does_not_change_nonletters():
    ''' get_next_letter should not change non letter characters '''
    assert get_next_letter(' ') == ' ', "spaces should be unchanged"
