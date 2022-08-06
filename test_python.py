from math import sqrt, pi, pow, hypot

from functiouns import fun, slovariq, list_1


def test_hypot_true():
    assert hypot(4, 3) == 5


def test_pi_true():
    assert round(pi, 2) == 3.14


def test_sqrt_true():
    assert sqrt(4) == 2


def test_pow_true():
    assert pow(4, 3) == 64


def test_map_func():
    assert list(map(fun, [2, 2, 3])) == [4, 4, 9]


def test_filter_func():
    assert list(filter(None, slovariq)) == [11, 18, 21, 12, 34, 0.1]


def test_sorted_func():
    assert list(sorted(list_1)) == [2, 2, 4, 5, 17, 23, 67]
