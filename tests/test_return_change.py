"""
Tests for the vending machine program, return change step
"""

import vending_machine

def test_no_change_required():
    assert vending_machine.return_change(0) == []
