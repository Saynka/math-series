from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series


# Fibonacci-test
def test_one():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_two():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_three():
    actual = fibonacci(8)
    expected = 21
    assert actual == expected

# lucas-test

def test_onel():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_twol():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_threel():
    actual = lucas(1)
    expected = 1
    assert actual == expected

# sum-series

def test_ones():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_twos():
    actual = sum_series(2)
    expected = 1
    assert actual == expected

def test_threes():
    actual = sum_series(5)
    expected = 5
    assert actual == expected
