"""
Tests for the vending machine program, but product step
"""
import pytest
import vending_machine

def test_buy_drink():
    """
    Asserts that a drink can be purchased
    """
    assert vending_machine.buy_product("drink", 275) == 0

def test_buy_banana():
    """
    Asserts that a value error is thrown when a banana is attempted to be purchased
    """
    with pytest.raises(ValueError):
        assert vending_machine.buy_product("banana", 275)

def test_buy_chips():
    """
    Asserts that chips can be purchased
    """
    assert vending_machine.buy_product("chips", 225) == 0

def test_buy_candy():
    """
    Asserts that a drink can be purchased
    """
    assert vending_machine.buy_product("candy", 315) == 0
