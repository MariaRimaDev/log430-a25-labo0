"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

# TODO: ajoutez les tests

"=========================== ACTIVITÉ 1 ==========================="

my_calculator = Calculator()

def test_addition():
    assert my_calculator.addition(2, 3) == 5

def test_subtraction():
    assert my_calculator.subtraction(5, 3) == 2

def test_multiplication():
    assert my_calculator.multiplication(4, 3) == 12

def test_division():
    assert my_calculator.division(10, 2) == 5

# def test_addition_erreur():
#     assert my_calculator.addition(2, 2) == 5