# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 20:40:54 2020

@author: raajesh.rameshbabu
"""

"""
Write a function using only list filter lambda that can tell 
whether a number is a Fibonacci number or not. 
You can use a pre-calculated list/dict to store fab numbers till 10000 PTS:100
"""

# A pre-calculated list to store fibonacci numbers till 10000
fibonacci_numbers = [0, 1]
while fibonacci_numbers[-1] + fibonacci_numbers[-2] < 10000:
    fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    
# A function using only list filter lambda that can tell whether a number is a Fibonacci number or not
check_fibonacci = lambda l : list(filter(lambda x: x in fibonacci_numbers, l))

check_fibonacci([1, 5, 333, 777, 1597, 6765, 8000])

#this is for testing with assert
def test_fibonacci():
    assert check_fibonacci([1, 5, 333, 777, 1597, 6765, 8000]) == [1, 5, 1597, 6765], "check_fibonacci is not correctly implemented!"    