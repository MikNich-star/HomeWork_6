from myfunctions import simple_separator, long_separator, separator, pow_many, my_filter


def test_simple_separator():
    assert simple_separator() == '**********'


def test_long_separator():
    assert long_separator(3) == '***'


def test_separator():
    assert separator('#', 5) == '#####'


def test_pow_many():
    assert pow_many(1, 1, 2) == 3


def test_my_filter():
    assert my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2]



