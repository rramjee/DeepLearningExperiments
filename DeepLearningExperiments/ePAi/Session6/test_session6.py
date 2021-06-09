import pytest
import random
import string
import session6
import os
import inspect
import re
import math
import importlib

DECK2= ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AS', '2C', '3C', '4C',
 '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AC', '2H', '3H', '4H', '5H', '6H',
  '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AH', '2D', '3D', '4D', '5D', '6D', '7D', '8D',
   '9D', 'TD', 'JD', 'QD', 'KD', 'AD']
DECK1 = ['2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S', '4C', '4D', '4H', '4S', '5C', '5D', '5H', '5S',
 '6C', '6D', '6H', '6S', '7C', '7D', '7H', '7S', '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S', 'AC',
  'AD', 'AH', 'AS', 'JC', 'JD', 'JH', 'JS', 'KC', 'KD', 'KH', 'KS', 'QC', 'QD', 'QH', 'QS', 'TC', 'TD', 'TH', 'TS']

README_CONTENT_CHECK_FOR = ["Royal flush","Straight flush", "Four of a kind","Full house","Flush","Straight","Three of a kind",
     "Two pair","One pair","High Card"]

CONTENT_CHECK_FOR = ['straight','straight_3cards','straight_4cards','flush','kind','two_pair','card_ranks']


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding = 'utf-8')
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 100 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding = 'utf-8')
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding = 'utf-8')
    content = f.read()
    f.close()
    assert content.count("#") >= 10

# def test_intentation():
#     """ Returns pass if used four spaces for each level of syntactically \
#     significant indenting."""
#     lines = inspect.getsource(session6)
#     spaces = re.findall("\n +.", lines)
#     for space in spaces:
#         assert re.search(
#             '[a-zA-Z#@""]', space
#         ), "Your code intentation does not follow PEP8 guidelines"
#         assert (
#             len(re.sub(r"[a-zA-Z#@\n\"\"]", "", space)) % 4 == 0
#         ), "Your code intentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_same_number_card():
    with pytest.raises(ValueError) as e_info:
        hands = (["AH","2H","3H","4H","5H"],["JS","JS","JS"])
        session6.poker(hands)

def test_length_of_card():
    with pytest.raises(ValueError) as e_info:
        hands = (["AH","2H"],["JS","JS"])
        session6.poker(hands)

def test_min_20_test_cases():
    """
    Test case to check at least minimum 20 test cases area are defined in
    test file.
    """
    mod = importlib.import_module("test_session6", os.path.abspath('.'))
    functions = inspect.getmembers(mod, inspect.isfunction)
    assert len(functions) >= 20


def test_function_doc_strings():
    """
    Test case to check the docstrings are included in the function definition.
    """
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert function[1].__doc__

def test_function_annotations():
    """
    Test case to check the function typing are implemented in the function
    definition.
    """
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert function[1].__annotations__


def test_deck_using_zip_lambda():
    """
    Test case to check the creation of cards using the lambda, zip and map
    `deck_using_deck_expression`. Validates using the manually created cards list.
    """
    
    assert session6.deck_function() == DECK1


def test_deck_using_for():
    """
    Test case to check the creation of cards by normal method using loops
    `deck_using_normal_way`. Validates using the manually created cards list.
    """
    assert session6.merge() == DECK2


def test_poker_function():
    hands = (['AH','KH','QH','JH','TH'],['TC','9C','8C','7C','6C'])
    assert '1' == session6.poker(hands)
    hands = (['TC','9C','8C','7C','6C'],['QC','QS','QD','QH','5C'])
    assert '1' == session6.poker(hands)
    hands = (['QC','QS','QD','QH','5C'],['AH','AC','AD','KC','KH'])
    assert '1' == session6.poker(hands)
    hands = (['AH','AC','AD','KC','KH'],['KC','8C','6C','4C','2C'])
    assert '1' == session6.poker(hands)
    hands = (['KC','8C','6C','4C','2C'],['8C','7K','6D','5H','4C'])
    assert '1' == session6.poker(hands)
    hands = (['8C','7K','6D','5H','4C'],['QC','QH','QS','7C','2H'])
    assert '1' == session6.poker(hands)
    hands = (['QC','QH','QS','7C','2H'],['JC','JD','9S','9C','5C'])
    assert '1' == session6.poker(hands)
    hands = (['JC','JD','9S','9C','5C'],['KC','KH','9S','8C','4H'])
    assert '1' == session6.poker(hands)
    hands = (['KC','KH','9S','8C','4H'],['AC','QH','6S','4C','2H'])
    assert '1' == session6.poker(hands)
    
    hands = (['AH','KH','QH','JH'],['TC','9C','8C','7C'])
    assert '1' == session6.poker(hands)
    hands = (['TC','9C','8C','7C'],['QC','QS','QD','QH'])
    assert '1' == session6.poker(hands)
    hands = (['KC','8C','6C','4C'],['8C','7K','6D','5H'])
    assert '1' == session6.poker(hands)
    hands = (['8C','7K','6D','5H'],['QC','QH','QS','7C'])
    assert '1' == session6.poker(hands)
    hands = (['QC','QH','QS','7C'],['JC','JD','9S','9C'])
    assert '1' == session6.poker(hands)
    hands = (['JC','JD','9S','9C'],['KC','KH','9S','8C'])
    assert '1' == session6.poker(hands)
    hands = (['KC','KH','9S','8C'],['AC','QH','6S','4C'])
    assert '1' == session6.poker(hands)
    hands = (['AH','KH','QH','JH'],['TC','9C','8C','7C'])
    
    
    hands = (['AH','KH','QH'],['TC','9C','8C'])
    assert '1' == session6.poker(hands)
    hands = (['KC','8C','6C'],['8C','7K','6D'])
    assert '1' == session6.poker(hands)
    hands = (['8C','7K','6D'],['QC','QH','QS'])
    assert '1' == session6.poker(hands)
    hands = (['KC','KH','9S'],['AC','QH','6S'])
    assert '1' == session6.poker(hands)

def test_tied():
    hands = (['AH','KH','QH','JH','TH'],['AS','KS','QS','JS','TS'])
    assert "HARD LUCK"== session6.poker(hands)
    

def test_file_contents():
    code_lines = inspect.getsource(session6)
    for word in CONTENT_CHECK_FOR:
        assert word in code_lines, 'Have you heard of Pinocchio?'

def test_straight_positive():
    hand = ['AS','KS','QS','JS','TS']
    rank = session6.card_ranks(hand)
    assert True == session6.straight(rank)

def test_straight_negative():
    hand = ['AS','KS','9S','JS','TS']
    rank = session6.card_ranks(hand)
    assert False == session6.straight(rank)


def test_straight_3cards_positive():
    hand = ['AS','KS','QS']
    rank = session6.card_ranks(hand)
    assert True == session6.straight_3cards(rank)

def test_straight_3cards_negative():
    hand = ['AS','9S','QS']
    rank = session6.card_ranks(hand)
    assert False == session6.straight_3cards(rank)

def test_straight_4cards_positive():
    hand = ['AS','KS','QS','JS']
    rank = session6.card_ranks(hand)
    assert True == session6.straight_4cards(rank)

def test_straight_4cards_negative():
    hand = ['AS','9S','TS','JS']
    rank = session6.card_ranks(hand)
    assert False == session6.straight_4cards(rank)

def test_flush_positive():
    hand =['AH','KH','QH','JH','TH']
    suits = session6.card_suits(hand)
    assert True == session6.flush(suits)

def test_flush_negative():
    hand =['AH','KH','7C','JH','TH']
    suits = session6.card_suits(hand)
    assert False == session6.flush(suits)