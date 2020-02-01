"""
Tests for the vending machine program
"""

import vending_machine

def test_five_cents():
    """
    Asserts that given a 5 cent coin, the vending machine receives the coin.
    """
    inserted_coins = []
    assert vending_machine.insert_coin(5, inserted_coins) == [5]
