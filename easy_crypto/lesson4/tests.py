from .homework import count_letter_a, count_letter


def test_count_letter_a():
    assert count_letter_a("hello") == 0
    assert count_letter_a("bondia") == 1
    assert count_letter_a("agora") == 2
    assert count_letter_a("aaaaaaaaaa") == 10


def test_count_letter():
    assert count_letter("hello", 'e') == 1
