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
    Assert that one quarter is returned when balance is 25.
    """
    assert vending_machine.return_change(25) == [25]

def test_balance_400_cents():
    """
    Assert that 2 x $2 are returned when change is 400.
    """
    assert vending_machine.return_change(400) == [200, 200]

def test_balance_300_cents():
    """
    Assert that 1 x $1 and 1 x $2 is returned when change is 300.
    """
    assert vending_machine.return_change(300) == [200, 100]

def test_balance_265_cents():
    """
    Assert that 1 x $2, 2 x $0.25, 1 x $0.10 and 1 x $0.05 is returned
    when change is 265.
    """
    assert vending_machine.return_change(265) == [200, 25, 25, 10, 5]

def test_balance_7_cents():
    """
    Assert that 7 cents is rounded down to 5 cents.
    """
    assert vending_machine.return_change(7) == [5]

def test_negative_balance():
    """
    Assert that negative values return no change.
    """
    assert vending_machine.return_change(-25) == []
