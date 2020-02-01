"""
Tests for the vending machine program, but product step
"""

import vending_machine

def test_buy_drink():
    assert vending_machine.buy_product('drink',275) == 0
