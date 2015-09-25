import pytest

from code import mysum


def test_1():
    assert mysum(1, 3) == 4


def test_2():
    assert mysum("Hello", "World") == "HelloWorld"


def test_an_exception():
    with pytest.raises(TypeError):
        mysum("Hello", 42)
