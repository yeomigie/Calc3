import pytest
from main import calculate

def test_add():
    assert calculate("5", "3", "add") == 8

def test_divide_by_zero():
    assert calculate("1", "0", "divide") == "Cannot divide by zero"

def test_unknown_operation():
    assert calculate("9", "3", "unknown") == "Unknown operation"
