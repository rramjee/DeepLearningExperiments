# EPAI Session 6, First Class Functions Part I

This session is about lambda expression , map function, filter , zip function. we also learn how to write lost comprehension and to write docstring and annotation.

In assignment we write a function for a game of poker.

[![poker.jpg](https://camo.githubusercontent.com/90e3dd5d22960855d5f4a8f56f3bdc0d1a30c841/68747470733a2f2f692e706f7374696d672e63632f664c64776e644e302f706f6b65722e6a7067)](https://postimg.cc/vgQR5cDQ)

# Here are the hands of poker

## Royal flush

A Royal Flush is a straight flush including the highest cards starting with ace and king, and this is the highest possible value when wild cards are not in use.

Cards must be: For 3 cards : Ace, King, Queen For 4 cards : Ace, King, Queen, Jack For 5 cards : Ace, King, Queen, Jack, 10

## Straight flush

Five cards in a sequence, all in the same suit. Ace can either come before 2 or come after King. A straight flush is a hand that contains five cards of sequential rank, all of the same suit, such as Q, J, 10, 9, 8.

Example: 3 cards : Queen, Jack, 10
4 cards : 10, 9, 8, 7
5 cards : 5, 4, 3, 2, Ace

## Four of a kind

All four cards of the same rank. Four of a kind, also known as quads, is a hand that contains four cards of one rank and one card of another rank (the kicker), such as 9, 9, 9, 9, J.

Example: 3 cards : Not Applicable
4 cards : 2, 2, 2, 2
5 cards : 9, 9, 9, 9, 6

## Full house

Three of a kind with a pair. A full house, also known as a full boat or a boat (and originally called a full hand), is a hand that contains three cards of one rank and two cards of another rank, such as 3, 3, 3, 6, 6.

Example: 3 cards : Not Applicable
4 cards : Not Applicable
5 cards : 7, 7, 7, 2, 2.

## Flush

Any five cards of the same suit, but not in a sequence.

## Straight

Five cards in a sequence, but not of the same suit. A straight is a hand that contains cards of sequential rank, not all of the same suit.

Example: 3 cards : 7, 6, 5
4 cards : 7, 6, 5, 4
5 cards : 7, 6, 5, 4, 3

## Three of a kind

Three cards of the same rank. Three of a kind, also known as trips or a set, is a hand that contains three cards of one rank and two cards of two other ranks (the kickers).

Example: 3 cards : 7, 7, 7
4 cards : 7, 7, 7, 4
5 cards : 7, 7, 7, 4, 3

## Two pair

Two different pairs. Two pair is a hand that contains two cards of one rank, two cards of another rank and one card of a third rank (the kicker).

Example: 3 cards : Not Applicable
4 cards : 7, 7, 4, 4
5 cards : 7, 7, 4, 4, 3

## Pair

Two cards of the same rank. One pair, or simply a pair, is a hand that contains two cards of one rank and three cards of three other ranks (the kickers).

Example: 3 cards : 4, 4, 6
4 cards : 4, 4, 5, 6
5 cards : 4, 4, 7, 8, 9

## High Card

When you haven’t made any of the hands above, the highest card plays. In the example below, the jack plays as the highest card. High card, also known as no pair or simply nothing, is a hand that does not fall into any other category.

Example: 3 cards : 4, 2, 6
4 cards : 4, 1, 5, 9
5 cards : 4, 5, 8, Queen, 9