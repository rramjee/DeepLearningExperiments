# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:33:54 2020

@author: raajesh.rameshbabu
"""

"""
Write the above again from scratch where KA can be changed to DL, 
and 1000/9999 ranges can be provided.  PTS:100
"""
import random
from functools import partial
# Partial function to let user input state ID and plate number
random_plates = lambda st='KA', number_plate='1234' : [f"{st}{random.randint(10, 99)}{chr(random.randint(65, 90))}{chr(random.randint(65, 90))}{number_plate}" for i in range(15)]

random_plates_partial = partial(random_plates, st = 'DL', number_plate = '7777')

all([x[:2]=="DL" and int(x[2:4]) in range(10, 100) and int(x[-4:]) == 7777 for x in random_plates('DL', 7777)])

def test_random_plates():
    assert all([x[:2]=="DL" and int(x[2:4]) in range(10, 100) and int(x[-4:]) == 7777 for x in random_plates('DL', 7777)])

