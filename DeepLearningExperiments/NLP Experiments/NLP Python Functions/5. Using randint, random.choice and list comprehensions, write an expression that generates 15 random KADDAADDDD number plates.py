# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:28:56 2020

@author: raajesh.rameshbabu
"""

"""
Using randint, random.choice and list comprehensions, 
write an expression that generates 15 random KADDAADDDD number plates, 
where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 
10<<DD<<99 & 1000<<DDDD<<9999 PTS:100
"""
import random
# An expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999
generate_number_plate = lambda : [f"KA{random.randint(10, 99)}{chr(random.randint(65, 90))}{chr(random.randint(65, 90))}{random.randint(1000, 9999)}" for i in range(15)]

all([x[:2]=="KA" and (int(x[2:4]) in range(10, 100)) and (int(x[-4:]) in range(1000, 10000)) for x in generate_number_plate()])

def test_generate_number_plate():
    assert all([x[:2]=="KA" and (int(x[2:4]) in range(10, 100)) and (int(x[-4:]) in range(1000, 10000)) for x in generate_number_plate()])
    
    