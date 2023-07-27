from collections.abc import Iterable
import pytest

@pytest.mark.parametrize("age", [34, 45])
def test_age(age):
    assert age > 0, "Age should be greater than zero"
    print(f"Your age is: {age}")


@pytest.mark.parametrize("num", [8])
def test_equal(num):
    assert num == 8, "Number are not equal"
    print(f"{num} == {num}")


@pytest.mark.parametrize("num", [12])
def test_not_equal(num):
    assert num != 10, "Numbers are equal"


@pytest.mark.parametrize("value", [4])
def test_type_is(value):
    assert type(value) is int, "Should be integer"


@pytest.mark.parametrize("value", [0.95])
def test_type_is_not(value):
    assert type(value) is not int, "Should not be integer"


@pytest.mark.parametrize("string", ["abc"])
def test_is_instance(string):
    assert isinstance(string, str)


def test_is_boolean():
    true = 8 == 8
    assert true is True


def test_is_not_boolean():
    true = 8 == 0
    assert true is False


def test_is_in():
    fruits = ["kiwi", "mango", "apple", "orange", "banana"]
    assert "mango" in fruits
    #assert "mango" not in fruits


def test_comparison():
    assert 5 > 2, "5 should be greatest"


def test_mod():
    assert 4 % 2 == 0, "Not even number"


def test_any():
    number = [5, 2, 7, 8]
    boolean = [False, True, False, False]
    assert any(number) == True, "Numbers should be greater than zero"
    assert any(boolean) == True, "At least one 'True' is required"


def test_all():
    number = [5, 2, 7, 8]
    boolean = [False, False, False]
    assert all(number), "All numbers should be greater than zero"
    assert all(boolean) == False, "Either all 'TRUE' or 'FALSE'"


def test_is_iterable():
    my_list = [4, 8, 6, 1, 0, 9]
    assert isinstance(my_list, Iterable)


def test_and():
    statement = 5 == 5 and 9 == 9
    assert statement == True, "Both conditions must be TRUE"


def test_or():
    statement = 5 != 5 or 'a' == 'a'
    assert statement, "Either of the condition is TRUE"