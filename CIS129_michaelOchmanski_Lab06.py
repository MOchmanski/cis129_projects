'''
CIS129_michaelOchmanski_lab06
Author: Michael Ochmanski
Version 1.0
Created 3/11/2025
Last Modified: 3/11/2025
Description: This program calculates the minimum amount of packages of hot
    dogs and the minimum amount of packages of hot dog buns needed for a
    cookout with the least amount of leftovers. 
'''

import math


def main():
    total = get_total_hot_dogs()

    # variables denote amt of item in a package
    dogs = 10
    buns = 8
    # rounded up to account for the total not being divisible by amt in package
    min_dogs = math.ceil(total / dogs)
    min_buns = math.ceil(total / dogs)
    # calculates leftover items
    dogs_left = (dogs - total % dogs) % dogs
    buns_left = (buns - total % buns) % buns

    show_results(dogs_left, min_dogs, buns_left, min_buns)

def get_total_hot_dogs():
    '''
    This function prompts inputs from the user to get the number of attendees
    and the number of hot dogs per attendee 
    Parameters: None
    Returns: 
        total - the total hot dogs needed
    '''
    people = int(input("Enter the number of people attending the cookout: "))
    hot_dogs = int(input("Enter the number of hot dogs for each person: "))
    total = people * hot_dogs
    return total

def show_results(dogs_left, min_dogs, buns_left, min_buns):
    '''
    This function calculates the minimum packages of hot dogs and hot dog buns
    needed for the cookout. 
    Parameters: 
        min_dogs - the minimum packages of hot dogs needed
        min_buns - the minimum packages of hot dog buns needed
        dogs_left - the leftover hot dogs
        buns_left - the leftover hot dog buns 
    Returns: 
        Displays the contents of each parameter

    '''
    print('Minimum packages of hot dogs needed:', min_dogs)
    print('Minimum packages of hot dog buns needed:', min_buns)
    print('Hot dogs left over:', dogs_left)
    print('Hot dog buns left over:', buns_left)

if __name__ == "__main__":
    main()