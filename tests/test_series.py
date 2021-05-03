import pytest

from math_series.series import fibonacci, lucas, sum_series

# Arrange, Act, Assert

def test_fibonacci():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_lucas():
    actual = lucas(4)
    expected = 7
    assert actual == expected

def test_sum_series_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_sum_series_two():
    actual = sum_series(2, 2, 1)
    expected = 3
    assert actual == expected

def test_sum_series_three():
    actual = sum_series(2, 4, 5)
    expected = 1
    assert actual == expected



