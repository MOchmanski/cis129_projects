'''
CIS129_michaelOchmanski_lab07
Author: Michael Ochmanski
Version 1.0
Created: 4/4/2025
Last Modified 4/4/2025
Description: This program takes the number of tickets sold in 3 different
seating sections and displays the total ticket sales.
'''


def main():
    #Declare integer constants
    seatsA, seatsB, seatsC = 300, 500, 200
    priceA, priceB, priceC = 20, 15, 10
    amt_of_sections = 3  #variable to stop the while loop
    #Declare string constants
    section1 = "Section A"
    section2 = "Section B"
    section3 = "Section C"
    #variables
    welcome_message = f'''This Dramatic Theater has {amt_of_sections} sections.
{section1} has {seatsA} seats at ${priceA} per seat.
{section2} has {seatsB} seats at ${priceB} per seat. 
{section3} has {seatsC} seats at ${priceC} per seat.'''
    oversell_message = "That's too many tickets. Time for some refunds!"
    msg = 'How many tickets were sold in this section: '
    #variable for input validation shielding against very large numbers
    #arbitrary addition to max seats to account for overselling
    max_ticket_sales = max(seatsA, seatsB, seatsC) + 200
    counter = 0
    subtotal = 0
    print(welcome_message)
    while counter < amt_of_sections:
        tickets = validate_ticket_number(msg, max_ticket_sales)
        if counter == 0:
            ticketsA = tickets
            subtotal += ticketsA * priceA
            print(f'the income for the tickets sold so far is ${subtotal}')
            if ticketsA > seatsA:
                print(oversell_message)
        if counter == 1:
            ticketsB = tickets
            subtotal += ticketsB * priceB
            print(f'the income for the tickets sold so far is ${subtotal}')
            if ticketsB > seatsB:
                print(oversell_message)
        if counter == 2:
            ticketsC = tickets 
            subtotal += ticketsC * priceC
            print(f'the income for the tickets sold so far is ${subtotal}')
            if ticketsC > seatsC:
                print(oversell_message)
        counter += 1
    print(f'The total income generated from ticket sales is {subtotal}')

def validate_ticket_number(msg, max_ticket_sales):
    '''
    This function validates the number of tickets sold is a valid number
    Parameters:
        msg - a string which contains the input prompt
        max_ticket_sales - an integer describing the feasible limit of ticket
            sales
    Returns:
        tickets - an integer describing the tickets sold in a specific section
    '''
    tickets = get_tickets_sold(msg)
    while tickets > max_ticket_sales:
        print("Invalid Value: Thats way too many tickets!")
        tickets = get_tickets_sold(msg)
    return tickets

def get_tickets_sold(msg):
    '''
    This function validates input of tickets sold is a usable integer
    Parameters:
        msg - a string which contains the input prompt
    Returns:
        value - an integer describing the user input for ticket sales
    '''
    counter = True
    while counter:
        value = input(msg)
        if ' ' in value:
            print("Invalid Value: Unexpected space")
        elif not value.isdigit():
            print("Invalid Value: Not a positive integer")
        else:
            value = int(value)
            counter = False
    return value

if __name__ == "__main__":
    main()
