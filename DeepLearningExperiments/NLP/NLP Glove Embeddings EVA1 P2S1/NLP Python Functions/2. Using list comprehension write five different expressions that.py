# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 20:52:44 2020

@author: raajesh.rameshbabu
"""

"""
Using list comprehension (and zip/lambda/etc if required) write five different expressions that: PTS:100
add 2 iterables a and b such that a is even and b is odd
strips every vowel from a string provided (tsai>>t s)
acts like a ReLU function for a 1D array
acts like a sigmoid function for a 1D array
takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
"""

# List comprehension to add 2 iterables a and b such that a is even and b is odd
add_even_odd = lambda a, b : [x + y for x, y in zip(a, b) if x % 2 == 0 and y % 2 != 0]

add_even_odd([4, 7, 10, 15, 20], [3, 6, 8, 1, 11])

#this is for testing using assert
def test_add_even_odd():
    assert add_even_odd([4, 7, 10, 15, 20], [3, 6, 8, 1, 11]) == [7, 31], "add_even_odd is not correctly implemented!"
    

# List comprehension to strip every vowel from a string provided
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', '0', 'U']
strip_vowels = lambda s : [x for x in s if x not in vowels]  

strip_vowels('tsai')

#this is for testing using assert
def test_strip_vowels():
    assert strip_vowels('tsai') == ['t', 's'], "strip_vowels is not correctly implemented!"  
    

# List comprehension to act like a ReLU function for a 1D array
relu_func = lambda l : [x if x > 0 else 0 for x in l]

relu_func([1.43, -0.76, 0.356, -1.89])   

def test_relu_func():
    assert relu_func([1.43, -0.76, 0.356, -1.89]) == [1.43, 0, 0.356, 0], "relu_func is not correctly implemented!"
    

# List comprehension to act like a sigmoid function for a 1D array
import math    
sigmoid_func = lambda l : [(1 / (1 + math.exp(-x))) for x in l]

sigmoid_func([1, 2, -3, -4, 0])

def test_sigmoid_func():
    assert sigmoid_func([1, 2, -3, -4, 0]) == [0.7310585786300049, 0.8807970779778823, 0.04742587317756678, 0.01798620996209156, 0.5], "sigmoid_func is not correctly implemented!"  
    


# List comprehension that takes a small character string and shifts all characters by 5
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
shift_characters = lambda s : "".join([alphabets[alphabets.index(x) + 5] if alphabets.index(x) < 21 else alphabets[alphabets.index(x) - 26 + 5] for x in s])    

shift_characters('tsai')

def test_shift_characters():
    assert shift_characters('tsai') == 'yxfn', "shift_characters is not correctly implemented!"
    assert shift_characters('zero') == 'ejwt', "shift_characters is not correctly implemented!"