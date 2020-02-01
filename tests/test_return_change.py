"""
Tests for the vending machine program, return change step
"""

import vending_machine

def test_no_change_required():
    """
    Assert that no change returned when balance is 0.
    """
    assert vending_machine.return_change(0) == []

def test_balance_25_cents():
    """
    Assert that no change returned when balance is 0.
    """
    assert vending_machine.return_change(25) == [25]
