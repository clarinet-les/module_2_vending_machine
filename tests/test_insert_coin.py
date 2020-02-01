"""
Tests for the vending machine program
"""
import pytest
import vending_machine

def test_five_cents():
    """
    Asserts that given a 5 cent coin, the vending machine receives the coin.
    """
    inserted_coins = []
    assert vending_machine.insert_coin(5, inserted_coins) == [5]

def test_fifty_cents():
    """
    Asserts that given a 50 cent coin, the vending machine will output
    an error since 50 cent coins are rare.
    """
    inserted_coins = []
    with pytest.raises(ValueError):
        vending_machine.insert_coin(50, inserted_coins)
