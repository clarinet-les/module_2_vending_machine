"""
A virtual vending machine.
"""
def insert_coin(coin, inserted_coins):
    """
    Function to add the newly inserted coin to the total for
    the already inserted coins.
    """
    valid_coins = [5, 10, 25, 100, 200]
    if coin not in valid_coins:
        raise ValueError

    inserted_coins.append(coin)
    return inserted_coins

def buy_product(product, balance):
    product_cost = {"drink":275, "candy":225, "chips":315}
    remaining_balance = balance - product_cost[product]
    return remaining_balance

class InsufficientFunds(Exception):
    """
    Exception used to indicate that there isn't
    enough money to make a purchase.
    """
    pass
