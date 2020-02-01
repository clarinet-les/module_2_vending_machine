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

def test_ten_cents():
    """
    Asserts that given a 10 cent coin, the vending machine receives the coin.
    """
    inserted_coins = []
    assert vending_machine.insert_coin(10, inserted_coins) == [10]

def test_twenty_five_cents():
    """
    Asserts that given a 25 cent coin, the vending machine receives the coin.
    """
    inserted_coins = []
    assert vending_machine.insert_coin(25, inserted_coins) == [25]

def test_one_dollar():
    """
    Asserts that given a 1 dollar coin, the vending machine receives the coin.
    """
    inserted_coins = []
    assert vending_machine.insert_coin(100, inserted_coins) == [100]

def test_two_dollars():
    """
    Asserts that given a 2 dollar coin, the vending machine receives the coin.
    """
    inserted_coins = []
    assert vending_machine.insert_coin(200, inserted_coins) == [200]

def test_coin_insertion():
    """
    Asserts that given a 5 cent coin, the vending machine receives the coin.
    """
    inserted_coins = [5, 100]
    assert vending_machine.insert_coin(25, inserted_coins) == [5, 100, 25]
