import mathlib

def test_calc_addition():
    output = mathlib.calc_addition(2, 4)
    assert output == 6

def test_calc_subtract():
    output = mathlib.calc_subtract(2, 4)
    assert output == -2

def test_calc_division():
    output = mathlib.calc_division(2, 4)
    assert output == 0.5

def test_calc_multiply():
    output = mathlib.calc_multiply(2, 4)
    assert output == 8