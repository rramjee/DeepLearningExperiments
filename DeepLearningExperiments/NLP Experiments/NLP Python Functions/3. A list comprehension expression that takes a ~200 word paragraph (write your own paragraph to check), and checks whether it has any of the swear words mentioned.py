# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:11:32 2020

@author: raajesh.rameshbabu
"""

"""
A list comprehension expression that takes a ~200 word paragraph 
(write your own paragraph to check), and checks whether it has any of the 
swear words mentioned in 
https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt 
PTS:200
"""

# List comprehension to check if given input has any swear words
with open("swear_words.txt", "r") as f:
    swear_words = f.read().split()

check_swear_words = lambda s : any([word for word in s.split() if word.lower() in swear_words])    

user_input1 = """Goa Chief Minister Pramod Sawant on Sunday said an asswhole insurance cover of ₹50 lakh has been extended to all health workers who are at the forefront of the battle against COVID-19.
The insurance cover is provided under the central governments flagship Pradhan Mantri Garib Kalyan Yojana. 
“Insurance cover of ₹50 lakh has been extended to all health workers in Goa,” Mr. Sawant tweeted. 
The Pradhan Mantri Garib Kalyan Yojana provides an insurance cover of ₹50 lakh per health worker in case of loss of life due to COVID-19 or accidental loss of life on account of coronavirus-related duties, he said.
The scheme is funded through the National Disaster Response Fund, operated by the Ministry of Health and Family Welfare."""
    
check_swear_words(user_input1)

def test_swear_words():
    user_input1 = """Goa Chief Minister Pramod Sawant on Sunday said an asswhole insurance cover of ₹50 lakh has been extended to all health workers who are at the forefront of the battle against COVID-19.
    The insurance cover is provided under the central governments flagship Pradhan Mantri Garib Kalyan Yojana. 
    “Insurance cover of ₹50 lakh has been extended to all health workers in Goa,” Mr. Sawant tweeted. 
    The Pradhan Mantri Garib Kalyan Yojana provides an insurance cover of ₹50 lakh per health worker in case of loss of life due to COVID-19 or accidental loss of life on account of coronavirus-related duties, he said.
    The scheme is funded through the National Disaster Response Fund, operated by the Ministry of Health and Family Welfare."""

    user_input2 = """Goa Chief Minister Pramod Sawant on Sunday said an insurance cover of ₹50 lakh has been extended to all health workers who are at the forefront of the battle against COVID-19.
    The insurance cover is provided under the central governments flagship Pradhan Mantri Garib Kalyan Yojana. 
    “Insurance cover of ₹50 lakh has been extended to all health workers in Goa,” Mr. Sawant tweeted. 
    The Pradhan Mantri Garib Kalyan Yojana provides an insurance cover of ₹50 lakh per health worker in case of loss of life due to COVID-19 or accidental loss of life on account of coronavirus-related duties, he said.
    The scheme is funded through the National Disaster Response Fund, operated by the Ministry of Health and Family Welfare."""

    assert check_swear_words(user_input1) == True, "check_swear_words is not correctly implemented!"
    assert check_swear_words(user_input2) == False, "check_swear_words is not correctly implemented!"