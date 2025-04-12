'''
cis129_michaelOchmanski_lab08.py
Author: Michael Ochmanski
Version 1.0
Created: 4/11/2025
Last Modified: 4/11/2025
Description: This program has one function that takes a string and determines
    whether or not said input is a palindrome.
'''


import math

def is_palindrome(string):
    '''
    This function determines whether or not a string is a palindrome
    Paramters:
        string - any string
    Returns:
        A True or False boolean value based on whether or not the string was a
        palindrome
    '''
    chars = []
    # creates a list where each index houses a single letter of input string
    for char in string:
        char = char.lower()
        if char not in ' .,?!;:':
            chars.append(char)
    # accounts for palindromes with an odd number of characters
    for char in range(math.floor(len(chars)/2)):
        if chars[char] != chars[-(char + 1)]:
            return False
    return True
