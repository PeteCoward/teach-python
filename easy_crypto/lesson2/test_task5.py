from .task5 import get_all_shifts


def test_get_all_shifts():
    assert get_all_shifts(bytearray([0])) == [bytearray([i % 256]) for i in range(1, 256)]
