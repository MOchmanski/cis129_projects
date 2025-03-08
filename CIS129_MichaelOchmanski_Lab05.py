'''
CIS129_MichaelOchmanski_Lab05.py
Author: Michael Ochmanski
Version 1.0
Created: 3/6/2025
Last Modified: 3/6/2025
Description: This program calculates the payout in dollars for the amount of
    bottles sold by the week.
'''


# declare local variables
keep_going = "y"

# loop to run program again
while keep_going == "y":
    # set value of variables
    counter = 0
    total_bottles = 0
    today_bottles = 0
    total_payout = 0
    while counter < 7:
        counter += 1
        today_bottles = int(input(f"Enter number of bottles for day #{counter}: "))
        total_bottles += today_bottles
        total_payout = total_bottles * 0.1
    print("The total number of bottles collected is", total_bottles)
    print("The total paid out is $", round(total_payout, 2), "\n")
    keep_going = input("Do you want to enter another week's worth of data?"
        "(Enter y or n)")
