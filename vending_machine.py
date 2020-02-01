"""
A virtual vending machine.
"""
VALID_COINS = [200, 100, 25, 10, 5]

def insert_coin(coin, inserted_coins):
    """
    Function to add the newly inserted coin to the total for
    the already inserted coins.
    """

    if coin not in VALID_COINS:
        raise ValueError

    inserted_coins.append(coin)
    return inserted_coins

def buy_product(product, balance):
    """
    Function to purchase drinks, candy and chips.
    """
    valid_products = ["drink", "candy", "chips"]
    if product not in valid_products:
        raise ValueError

    product_cost = {"drink":275, "chips":225, "candy":315}

    if product_cost[product] > balance:
        raise InsufficientFunds

    remaining_balance = balance - product_cost[product]
    return remaining_balance

def return_change(balance):
    """
    Function to return change to customer.
    """
    remaining_balance = balance
    change = []

    for i in VALID_COINS:
        number_coins = remaining_balance // i
        remaining_balance = remaining_balance % i
        change.extend([i for a in range(number_coins)])

    return change

class InsufficientFunds(Exception):
    """
    Exception used to indicate that there isn't
    enough money to make a purchase.
    """
