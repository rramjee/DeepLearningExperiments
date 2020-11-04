# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:18:23 2020

@author: raajesh.rameshbabu
"""

"""
Using reduce functions: PTS:100
add only even numbers in a list
find the biggest character in a string (printable ascii characters)
adds every 3rd number in a list
"""
from functools import reduce

# Reduce function to add only even numbers in a list
add_even_numbers = lambda l : reduce(lambda a, b: a + b if b % 2 == 0 else a, l, 0)
add_even_numbers([10, 15, 17, 20, 33, 40])
def test_add_even_numbers():
    assert add_even_numbers([10, 15, 17, 20, 33, 40]) == 70, "add_even_numbers is not correctly implemented!"    

# Reduce function to find the biggest character in a string
find_biggest_character = lambda s : reduce(lambda x, y: x if ord(x) > ord(y) else y, s)    
find_biggest_character("RaajeshLaguduvaRameshbabu")
def test_find_biggest_character():
    assert find_biggest_character("RaajeshLaguduvaRameshbabu") == 'r', "find_biggest_character is not correctly implemented!"
    
# Reduce function to add every 3rd number in a list
add_third_element = lambda l : reduce(lambda x, y: x + y, l[2::3], 0)
add_third_element([1, 2, 3, 4, 5, 6]) 
def test_add_third_element():
    assert add_third_element([1, 2, 3, 4, 5, 6]) == 9, "add_third_element is not correctly implemented!"