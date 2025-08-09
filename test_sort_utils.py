from sort_utils import sort_numbers


def test_sort_numbers_sorts_integers():
    assert sort_numbers([5, 3, 7, 1, 0]) == [0, 1, 3, 5, 7]

