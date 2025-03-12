''' 
cis129_lab03_coffeeShop.py
Description: This program intakes the number of muffins and cups of coffee
    that a customer will buy and returns a simple receipt of the total bill.
Author: Michael Ochmanski
Version: 1.3
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
    taco_count = input("How many tacos would you like to buy?")
    horchata_count = input(
        "Last but certainly not least, how much horchata would you like?"
        )
    # redundant variable to insure function only returns one item
    item_count = (coffee_count, muffin_count, taco_count, horchata_count)  
    return item_count

def bill_calculation(item_count):
    '''
    This function determines the values that will be placed on the receipt

    Parameters:
    items_count -- a list containing the cups of coffee purchased and the
    muffins sold

    Returns: 
    receipt_items -- a list containing the values of items that will be placed
    on the receipt
    '''
    # converting to float for price calculation
    coffee_count = float(item_count[0])
    muffin_count = float(item_count[1])
    taco_count = float(item_count[2])
    horchata_count = float(item_count[3])
    coffee_price = coffee_count * 3.5 
    muffin_price = muffin_count * 2
    taco_price = taco_count * 2.5
    horchata_price = horchata_count * 3
    subtotal = coffee_price + muffin_price + taco_price + horchata_price
    tax = round(subtotal * 0.06, 2) # round to fit monetary writing conventions
    total_cost = subtotal + tax
    receipt_items = (coffee_price, muffin_price, taco_price, 
                     horchata_price, tax, total_cost)
    return receipt_items

def print_receipt(item_count, receipt_items):
    '''
    This function consolidates all the information gathered in the other two
    functions and prints a receipt, mutable based on said information.

    Parameters: 
    item_count -- a list containing the cups of coffee purchased and the
    muffins sold
    receipt_items -- receipt_items -- a list containing the values of items that will be placed
    on the receipt

    Returns:
    receipt -- a receipt housing the previously gathered information
    '''
    coffee_count = item_count[0]
    muffin_count = item_count[1]
    taco_count = item_count[2]
    horchata_count = item_count[3]
    coffee_price = format(receipt_items[0], '.2f')  # mimics style of menu cost
    muffin_price = format(receipt_items[1], '.2f')
    taco_price = format(receipt_items[2], '.2f')
    horchata_price = format(receipt_items[3], '.2f')
    # as a precaution of the tax amount being divisble by 10
    tax = format(receipt_items[4], '.2f')
    total_cost = format(receipt_items[5], '.2f')
    receipt = f'''***************************************
Welcome to Java Nice Day Taco Truck & Cafe!
Number of coffees bought
{coffee_count}
Number of muffins bought
{muffin_count}
Number of tacos bought
{taco_count}
Number of horchata bought
{horchata_count}
***************************************

***************************************
Java Nice Day Taco Truck & Cafe Receipt
{coffee_count} Coffee at $3.50 each: $ {coffee_price}
{muffin_count} Muffins at $2.00 each: $ {muffin_price}
{taco_count} Tacos at $2.50 each: $ {taco_price}
{horchata_count} Horchata at $3.00 each: $ {horchata_price}
6% tax: $ {tax}
---------
Total: $ {total_cost}
***************************************
Have a nice day! Please come again :)
'''
    return receipt

def main():
    item_count = coffee_shop_order()
    receipt_items = bill_calculation(item_count)
    receipt = print_receipt(item_count, receipt_items)
    print(receipt)

if __name__ == "__main__":
    main()
