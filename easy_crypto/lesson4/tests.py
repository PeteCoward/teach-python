from .homework import count_letter_a


def test_count_letter_a():
    assert count_letter_a("hello") == 0
    assert count_letter_a("bondia") == 1
    assert count_letter_a("agora") == 2
