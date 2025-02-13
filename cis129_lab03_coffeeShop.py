''' 
cis129_lab03_coffeeShop.py
Description: This program intakes the number of muffins and cups of coffee
    that a customer will buy and returns a simple reciept of the total bill.
Author: Michael Ochmanski
Version: 1.0
Created: 2/13/2025
Last Modified: 2/13/2025
'''


def coffee_shop_order():
    '''
    This function takes user input to determine the amount of muffins and cups
    of coffee purchased
    
    Parameters: None

    Returns:
    items_count -- a list containing the amount of different items purchased 
    '''
    coffee_count = input("How many cups of coffee would you like?")
    muffin_count = input("How many muffins do you want to buy?")
    item_count = (coffee_count, muffin_count)  # function only returns one item
    return item_count

def bill_calculation(item_count):
    '''
    This function determines the values that will be placed on the reciept

    Parameters:
    items_count -- a list containing the cups of coffee purchased and the
    muffins sold

    Returns: 
    reciept_items -- a list containing the values of items that will be placed
    on the reciept
    '''
    coffee_count = float(item_count[0])
    muffin_count = float(item_count[1])
    coffee_price = coffee_count * 5 
    muffin_price = muffin_count * 4
    subtotal = coffee_price + muffin_price
    tax = round(subtotal * 0.06, 2)
    total_cost = subtotal + tax
    reciept_items = (coffee_price, muffin_price, tax, total_cost)
    return reciept_items

def print_reciept(item_count, reciept_items):
    '''
    This function consolidates all the information gathered in the other two
    functions and prints a reciept, mutable based on said information.

    Parameters: 
    item_count -- a list containing the cups of coffee purchased and the
    muffins sold
    reciept_items -- reciept_items -- a list containing the values of items that will be placed
    on the reciept

    Returns:
    reciept -- a reciept housing the previously gathered information
    '''
    coffee_count = item_count[0]
    muffin_count = item_count[1]
    coffee_price = format(reciept_items[0], '.2f')  # mimics style of menu cost
    muffin_price = format(reciept_items[1], '.2f')
    tax = round(reciept_items[2], 2)
    total_cost = reciept_items[3]
    reciept = f'''***************************************
    My Coffee and Muffin Shop
    Number of coffees bought?
    {coffee_count}
    Number of muffins bought?
    {muffin_count}
    ***************************************

    ***************************************
    My Coffee and Muffin Shop Receipt
    {coffee_count} Coffee at $5 each: $ {coffee_price}
    2 Muffins at $4 each: $ {muffin_price}
    6% tax: $ {tax}
    ---------
    Total: $ {total_cost}
    ***************************************
    '''
    return reciept

def main():
    item_count = coffee_shop_order()
    reciept_items = bill_calculation(item_count)
    reciept = print_reciept(item_count, reciept_items)
    print(reciept)

if __name__ == "__main__":
    main()
