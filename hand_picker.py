import random
import functools
from tkinter import *
from itertools import combinations
from treys import Card, Deck, Evaluator


def purge_offsuits(item):
	a, b = item
	return Card.get_suit_int(a) == Card.get_suit_int(b)


def purge_suits(item):
	a, b = item
	return Card.get_suit_int(a) != Card.get_suit_int(b)


SUITS = 'hsdc'
ACES = sorted({Card.new('A'+suit) for suit in SUITS}, reverse=True)
KINGS = sorted({Card.new('K'+suit) for suit in SUITS}, reverse=True)
QUEENS = sorted({Card.new('Q'+suit) for suit in SUITS}, reverse=True)
JACKS = sorted({Card.new('J'+suit) for suit in SUITS}, reverse=True)
TENS = sorted({Card.new('T'+suit) for suit in SUITS}, reverse=True)
NINES = sorted({Card.new('9'+suit) for suit in SUITS}, reverse=True)
EIGHTS = sorted({Card.new('8'+suit) for suit in SUITS}, reverse=True)
SEVENS = sorted({Card.new('7'+suit) for suit in SUITS}, reverse=True)
SIXES = sorted({Card.new('6'+suit) for suit in SUITS}, reverse=True)
FIVES = sorted({Card.new('5'+suit) for suit in SUITS}, reverse=True)
FOURS = sorted({Card.new('4'+suit) for suit in SUITS}, reverse=True)
THREES = sorted({Card.new('3'+suit) for suit in SUITS}, reverse=True)
TWOS = sorted({Card.new('2'+suit) for suit in SUITS}, reverse=True)


# Pockets
hAA = set(combinations(ACES, 2))
hKK = set(combinations(KINGS, 2))
hQQ = set(combinations(QUEENS, 2))
hJJ = set(combinations(JACKS, 2))
hTT = set(combinations(TENS, 2))
h99 = set(combinations(NINES, 2))
h88 = set(combinations(EIGHTS, 2))
h77 = set(combinations(SEVENS, 2))
h66 = set(combinations(SIXES, 2))
h55 = set(combinations(FIVES, 2))
h44 = set(combinations(FOURS, 2))
h33 = set(combinations(THREES, 2))
h22 = set(combinations(TWOS, 2))


# Suits
hAKs = set(filter(purge_offsuits, set(combinations(sorted(set().union(ACES, KINGS), reverse=True), 2)))) - hAA - hKK
hAQs = set(filter(purge_offsuits, set(combinations(sorted(set().union(ACES, QUEENS), reverse=True), 2)))) - hAA - hQQ
hAJs = set(filter(purge_offsuits, set(combinations(sorted(set().union(ACES, JACKS), reverse=True), 2)))) - hAA - hJJ
hATs = set(filter(purge_offsuits, set(combinations(sorted(set().union(ACES, TENS), reverse=True), 2)))) - hAA - hTT
hA9s = set(filter(purge_offsuits, set(combinations(sorted(set().union(ACES, NINES), reverse=True), 2)))) - hAA - h99
hA8s = set(filter(purge_offsuits, set(combinations(sorted(set().union(ACES, EIGHTS), reverse=True), 2)))) - hAA - h88
hA7s = set(filter(purge_offsuits, set(combinations(sorted(set().union(ACES, SEVENS), reverse=True), 2)))) - hAA - h77
hA6s = set(filter(purge_offsuits, set(combinations(sorted(set().union(ACES, SIXES), reverse=True), 2)))) - hAA - h66
hA5s = set(filter(purge_offsuits, set(combinations(sorted(set().union(ACES, FIVES), reverse=True), 2)))) - hAA - h55
hA4s = set(filter(purge_offsuits, set(combinations(sorted(set().union(ACES, FOURS), reverse=True), 2)))) - hAA - h44
hA3s = set(filter(purge_offsuits, set(combinations(sorted(set().union(ACES, THREES), reverse=True), 2)))) - hAA - h33
hA2s = set(filter(purge_offsuits, set(combinations(sorted(set().union(ACES, TWOS), reverse=True), 2)))) - hAA - h22


hKQs = set(filter(purge_offsuits, set(combinations(sorted(set().union(KINGS, QUEENS), reverse=True), 2)))) - hKK - hQQ
hKJs = set(filter(purge_offsuits, set(combinations(sorted(set().union(KINGS, JACKS), reverse=True), 2)))) - hKK - hJJ
hKTs = set(filter(purge_offsuits, set(combinations(sorted(set().union(KINGS, TENS), reverse=True), 2)))) - hKK - hTT
hK9s = set(filter(purge_offsuits, set(combinations(sorted(set().union(KINGS, NINES), reverse=True), 2)))) - hKK - h99
hK8s = set(filter(purge_offsuits, set(combinations(sorted(set().union(KINGS, EIGHTS), reverse=True), 2)))) - hKK - h88
hK7s = set(filter(purge_offsuits, set(combinations(sorted(set().union(KINGS, SEVENS), reverse=True), 2)))) - hKK - h77
hK6s = set(filter(purge_offsuits, set(combinations(sorted(set().union(KINGS, SIXES), reverse=True), 2)))) - hKK - h66
hK5s = set(filter(purge_offsuits, set(combinations(sorted(set().union(KINGS, FIVES), reverse=True), 2)))) - hKK - h55
hK4s = set(filter(purge_offsuits, set(combinations(sorted(set().union(KINGS, FOURS), reverse=True), 2)))) - hKK - h44
hK3s = set(filter(purge_offsuits, set(combinations(sorted(set().union(KINGS, THREES), reverse=True), 2)))) - hKK - h33
hK2s = set(filter(purge_offsuits, set(combinations(sorted(set().union(KINGS, TWOS), reverse=True), 2)))) - hKK - h22


hQJs = set(filter(purge_offsuits, set(combinations(sorted(set().union(QUEENS, JACKS), reverse=True), 2)))) - hQQ - hJJ
hQTs = set(filter(purge_offsuits, set(combinations(sorted(set().union(QUEENS, TENS), reverse=True), 2)))) - hQQ - hTT
hQ9s = set(filter(purge_offsuits, set(combinations(sorted(set().union(QUEENS, NINES), reverse=True), 2)))) - hQQ - h99
hQ8s = set(filter(purge_offsuits, set(combinations(sorted(set().union(QUEENS, EIGHTS), reverse=True), 2)))) - hQQ - h88
hQ7s = set(filter(purge_offsuits, set(combinations(sorted(set().union(QUEENS, SEVENS), reverse=True), 2)))) - hQQ - h77
hQ6s = set(filter(purge_offsuits, set(combinations(sorted(set().union(QUEENS, SIXES), reverse=True), 2)))) - hQQ - h66
hQ5s = set(filter(purge_offsuits, set(combinations(sorted(set().union(QUEENS, FIVES), reverse=True), 2)))) - hQQ - h55
hQ4s = set(filter(purge_offsuits, set(combinations(sorted(set().union(QUEENS, FOURS), reverse=True), 2)))) - hQQ - h44
hQ3s = set(filter(purge_offsuits, set(combinations(sorted(set().union(QUEENS, THREES), reverse=True), 2)))) - hQQ - h33
hQ2s = set(filter(purge_offsuits, set(combinations(sorted(set().union(QUEENS, TWOS), reverse=True), 2)))) - hQQ - h22


hJTs = set(filter(purge_offsuits, set(combinations(sorted(set().union(JACKS, TENS), reverse=True), 2)))) - hJJ - hTT
hJ9s = set(filter(purge_offsuits, set(combinations(sorted(set().union(JACKS, NINES), reverse=True), 2)))) - hJJ - h99
hJ8s = set(filter(purge_offsuits, set(combinations(sorted(set().union(JACKS, EIGHTS), reverse=True), 2)))) - hJJ - h88
hJ7s = set(filter(purge_offsuits, set(combinations(sorted(set().union(JACKS, SEVENS), reverse=True), 2)))) - hJJ - h77
hJ6s = set(filter(purge_offsuits, set(combinations(sorted(set().union(JACKS, SIXES), reverse=True), 2)))) - hJJ - h66
hJ5s = set(filter(purge_offsuits, set(combinations(sorted(set().union(JACKS, FIVES), reverse=True), 2)))) - hJJ - h55
hJ4s = set(filter(purge_offsuits, set(combinations(sorted(set().union(JACKS, FOURS), reverse=True), 2)))) - hJJ - h44
hJ3s = set(filter(purge_offsuits, set(combinations(sorted(set().union(JACKS, THREES), reverse=True), 2)))) - hJJ - h33
hJ2s = set(filter(purge_offsuits, set(combinations(sorted(set().union(JACKS, TWOS), reverse=True), 2)))) - hJJ - h22


hT9s = set(filter(purge_offsuits, set(combinations(sorted(set().union(TENS, NINES), reverse=True), 2)))) - hTT - h99
hT8s = set(filter(purge_offsuits, set(combinations(sorted(set().union(TENS, EIGHTS), reverse=True), 2)))) - hTT - h88
hT7s = set(filter(purge_offsuits, set(combinations(sorted(set().union(TENS, SEVENS), reverse=True), 2)))) - hTT - h77
hT6s = set(filter(purge_offsuits, set(combinations(sorted(set().union(TENS, SIXES), reverse=True), 2)))) - hTT - h66
hT5s = set(filter(purge_offsuits, set(combinations(sorted(set().union(TENS, FIVES), reverse=True), 2)))) - hTT - h55
hT4s = set(filter(purge_offsuits, set(combinations(sorted(set().union(TENS, FOURS), reverse=True), 2)))) - hTT - h44
hT3s = set(filter(purge_offsuits, set(combinations(sorted(set().union(TENS, THREES), reverse=True), 2)))) - hTT - h33
hT2s = set(filter(purge_offsuits, set(combinations(sorted(set().union(TENS, TWOS), reverse=True), 2)))) - hTT - h22


h98s = set(filter(purge_offsuits, set(combinations(sorted(set().union(NINES, EIGHTS), reverse=True), 2)))) - h99 - h88
h97s = set(filter(purge_offsuits, set(combinations(sorted(set().union(NINES, SEVENS), reverse=True), 2)))) - h99 - h77
h96s = set(filter(purge_offsuits, set(combinations(sorted(set().union(NINES, SIXES), reverse=True), 2)))) - h99 - h66
h95s = set(filter(purge_offsuits, set(combinations(sorted(set().union(NINES, FIVES), reverse=True), 2)))) - h99 - h55
h94s = set(filter(purge_offsuits, set(combinations(sorted(set().union(NINES, FOURS), reverse=True), 2)))) - h99 - h44
h93s = set(filter(purge_offsuits, set(combinations(sorted(set().union(NINES, THREES), reverse=True), 2)))) - h99 - h33
h92s = set(filter(purge_offsuits, set(combinations(sorted(set().union(NINES, TWOS), reverse=True), 2)))) - h99 - h22


h87s = set(filter(purge_offsuits, set(combinations(sorted(set().union(EIGHTS, SEVENS), reverse=True), 2)))) - h88 - h77
h86s = set(filter(purge_offsuits, set(combinations(sorted(set().union(EIGHTS, SIXES), reverse=True), 2)))) - h88 - h66
h85s = set(filter(purge_offsuits, set(combinations(sorted(set().union(EIGHTS, FIVES), reverse=True), 2)))) - h88 - h55
h84s = set(filter(purge_offsuits, set(combinations(sorted(set().union(EIGHTS, FOURS), reverse=True), 2)))) - h88 - h44
h83s = set(filter(purge_offsuits, set(combinations(sorted(set().union(EIGHTS, THREES), reverse=True), 2)))) - h88 - h33
h82s = set(filter(purge_offsuits, set(combinations(sorted(set().union(EIGHTS, TWOS), reverse=True), 2)))) - h88 - h22


h76s = set(filter(purge_offsuits, set(combinations(sorted(set().union(SEVENS, SIXES), reverse=True), 2)))) - h77 - h66
h75s = set(filter(purge_offsuits, set(combinations(sorted(set().union(SEVENS, FIVES), reverse=True), 2)))) - h77 - h55
h74s = set(filter(purge_offsuits, set(combinations(sorted(set().union(SEVENS, FOURS), reverse=True), 2)))) - h77 - h44
h73s = set(filter(purge_offsuits, set(combinations(sorted(set().union(SEVENS, THREES), reverse=True), 2)))) - h77 - h33
h72s = set(filter(purge_offsuits, set(combinations(sorted(set().union(SEVENS, TWOS), reverse=True), 2)))) - h77 - h22


h65s = set(filter(purge_offsuits, set(combinations(sorted(set().union(SIXES, FIVES), reverse=True), 2)))) - h66 - h55
h64s = set(filter(purge_offsuits, set(combinations(sorted(set().union(SIXES, FOURS), reverse=True), 2)))) - h66 - h44
h63s = set(filter(purge_offsuits, set(combinations(sorted(set().union(SIXES, THREES), reverse=True), 2)))) - h66 - h33
h62s = set(filter(purge_offsuits, set(combinations(sorted(set().union(SIXES, TWOS), reverse=True), 2)))) - h66 - h22


h54s = set(filter(purge_offsuits, set(combinations(sorted(set().union(FIVES, FOURS), reverse=True), 2)))) - h55 - h44
h53s = set(filter(purge_offsuits, set(combinations(sorted(set().union(FIVES, THREES), reverse=True), 2)))) - h55 - h33
h52s = set(filter(purge_offsuits, set(combinations(sorted(set().union(FIVES, TWOS), reverse=True), 2)))) - h55 - h22


h43s = set(filter(purge_offsuits, set(combinations(sorted(set().union(FOURS, THREES), reverse=True), 2)))) - h44 - h33
h42s = set(filter(purge_offsuits, set(combinations(sorted(set().union(FOURS, TWOS), reverse=True), 2)))) - h44 - h22


h32s = set(filter(purge_offsuits, set(combinations(sorted(set().union(THREES, TWOS), reverse=True), 2)))) - h33 - h22


# Off-Suits
hAKo = set(filter(purge_suits, set(combinations(sorted(set().union(ACES, KINGS), reverse=True), 2)))) - hAA - hKK
hAQo = set(filter(purge_suits, set(combinations(sorted(set().union(ACES, QUEENS), reverse=True), 2)))) - hAA - hQQ
hAJo = set(filter(purge_suits, set(combinations(sorted(set().union(ACES, JACKS), reverse=True), 2)))) - hAA - hJJ
hATo = set(filter(purge_suits, set(combinations(sorted(set().union(ACES, TENS), reverse=True), 2)))) - hAA - hTT
hA9o = set(filter(purge_suits, set(combinations(sorted(set().union(ACES, NINES), reverse=True), 2)))) - hAA - h99
hA8o = set(filter(purge_suits, set(combinations(sorted(set().union(ACES, EIGHTS), reverse=True), 2)))) - hAA - h88
hA7o = set(filter(purge_suits, set(combinations(sorted(set().union(ACES, SEVENS), reverse=True), 2)))) - hAA - h77
hA6o = set(filter(purge_suits, set(combinations(sorted(set().union(ACES, SIXES), reverse=True), 2)))) - hAA - h66
hA5o = set(filter(purge_suits, set(combinations(sorted(set().union(ACES, FIVES), reverse=True), 2)))) - hAA - h55
hA4o = set(filter(purge_suits, set(combinations(sorted(set().union(ACES, FOURS), reverse=True), 2)))) - hAA - h44
hA3o = set(filter(purge_suits, set(combinations(sorted(set().union(ACES, THREES), reverse=True), 2)))) - hAA - h33
hA2o = set(filter(purge_suits, set(combinations(sorted(set().union(ACES, TWOS), reverse=True), 2)))) - hAA - h22


hKQo = set(filter(purge_suits, set(combinations(sorted(set().union(KINGS, QUEENS), reverse=True), 2)))) - hKK - hQQ
hKJo = set(filter(purge_suits, set(combinations(sorted(set().union(KINGS, JACKS), reverse=True), 2)))) - hKK - hJJ
hKTo = set(filter(purge_suits, set(combinations(sorted(set().union(KINGS, TENS), reverse=True), 2)))) - hKK - hTT
hK9o = set(filter(purge_suits, set(combinations(sorted(set().union(KINGS, NINES), reverse=True), 2)))) - hKK - h99
hK8o = set(filter(purge_suits, set(combinations(sorted(set().union(KINGS, EIGHTS), reverse=True), 2)))) - hKK - h88
hK7o = set(filter(purge_suits, set(combinations(sorted(set().union(KINGS, SEVENS), reverse=True), 2)))) - hKK - h77
hK6o = set(filter(purge_suits, set(combinations(sorted(set().union(KINGS, SIXES), reverse=True), 2)))) - hKK - h66
hK5o = set(filter(purge_suits, set(combinations(sorted(set().union(KINGS, FIVES), reverse=True), 2)))) - hKK - h55
hK4o = set(filter(purge_suits, set(combinations(sorted(set().union(KINGS, FOURS), reverse=True), 2)))) - hKK - h44
hK3o = set(filter(purge_suits, set(combinations(sorted(set().union(KINGS, THREES), reverse=True), 2)))) - hKK - h33
hK2o = set(filter(purge_suits, set(combinations(sorted(set().union(KINGS, TWOS), reverse=True), 2)))) - hKK - h22


hQJo = set(filter(purge_suits, set(combinations(sorted(set().union(QUEENS, JACKS), reverse=True), 2)))) - hQQ - hJJ
hQTo = set(filter(purge_suits, set(combinations(sorted(set().union(QUEENS, TENS), reverse=True), 2)))) - hQQ - hTT
hQ9o = set(filter(purge_suits, set(combinations(sorted(set().union(QUEENS, NINES), reverse=True), 2)))) - hQQ - h99
hQ8o = set(filter(purge_suits, set(combinations(sorted(set().union(QUEENS, EIGHTS), reverse=True), 2)))) - hQQ - h88
hQ7o = set(filter(purge_suits, set(combinations(sorted(set().union(QUEENS, SEVENS), reverse=True), 2)))) - hQQ - h77
hQ6o = set(filter(purge_suits, set(combinations(sorted(set().union(QUEENS, SIXES), reverse=True), 2)))) - hQQ - h66
hQ5o = set(filter(purge_suits, set(combinations(sorted(set().union(QUEENS, FIVES), reverse=True), 2)))) - hQQ - h55
hQ4o = set(filter(purge_suits, set(combinations(sorted(set().union(QUEENS, FOURS), reverse=True), 2)))) - hQQ - h44
hQ3o = set(filter(purge_suits, set(combinations(sorted(set().union(QUEENS, THREES), reverse=True), 2)))) - hQQ - h33
hQ2o = set(filter(purge_suits, set(combinations(sorted(set().union(QUEENS, TWOS), reverse=True), 2)))) - hQQ - h22


hJTo = set(filter(purge_suits, set(combinations(sorted(set().union(JACKS, TENS), reverse=True), 2)))) - hJJ - hTT
hJ9o = set(filter(purge_suits, set(combinations(sorted(set().union(JACKS, NINES), reverse=True), 2)))) - hJJ - h99
hJ8o = set(filter(purge_suits, set(combinations(sorted(set().union(JACKS, EIGHTS), reverse=True), 2)))) - hJJ - h88
hJ7o = set(filter(purge_suits, set(combinations(sorted(set().union(JACKS, SEVENS), reverse=True), 2)))) - hJJ - h77
hJ6o = set(filter(purge_suits, set(combinations(sorted(set().union(JACKS, SIXES), reverse=True), 2)))) - hJJ - h66
hJ5o = set(filter(purge_suits, set(combinations(sorted(set().union(JACKS, FIVES), reverse=True), 2)))) - hJJ - h55
hJ4o = set(filter(purge_suits, set(combinations(sorted(set().union(JACKS, FOURS), reverse=True), 2)))) - hJJ - h44
hJ3o = set(filter(purge_suits, set(combinations(sorted(set().union(JACKS, THREES), reverse=True), 2)))) - hJJ - h33
hJ2o = set(filter(purge_suits, set(combinations(sorted(set().union(JACKS, TWOS), reverse=True), 2)))) - hJJ - h22


hT9o = set(filter(purge_suits, set(combinations(sorted(set().union(TENS, NINES), reverse=True), 2)))) - hTT - h99
hT8o = set(filter(purge_suits, set(combinations(sorted(set().union(TENS, EIGHTS), reverse=True), 2)))) - hTT - h88
hT7o = set(filter(purge_suits, set(combinations(sorted(set().union(TENS, SEVENS), reverse=True), 2)))) - hTT - h77
hT6o = set(filter(purge_suits, set(combinations(sorted(set().union(TENS, SIXES), reverse=True), 2)))) - hTT - h66
hT5o = set(filter(purge_suits, set(combinations(sorted(set().union(TENS, FIVES), reverse=True), 2)))) - hTT - h55
hT4o = set(filter(purge_suits, set(combinations(sorted(set().union(TENS, FOURS), reverse=True), 2)))) - hTT - h44
hT3o = set(filter(purge_suits, set(combinations(sorted(set().union(TENS, THREES), reverse=True), 2)))) - hTT - h33
hT2o = set(filter(purge_suits, set(combinations(sorted(set().union(TENS, TWOS), reverse=True), 2)))) - hTT - h22


h98o = set(filter(purge_suits, set(combinations(sorted(set().union(NINES, EIGHTS), reverse=True), 2)))) - h99 - h88
h97o = set(filter(purge_suits, set(combinations(sorted(set().union(NINES, SEVENS), reverse=True), 2)))) - h99 - h77
h96o = set(filter(purge_suits, set(combinations(sorted(set().union(NINES, SIXES), reverse=True), 2)))) - h99 - h66
h95o = set(filter(purge_suits, set(combinations(sorted(set().union(NINES, FIVES), reverse=True), 2)))) - h99 - h55
h94o = set(filter(purge_suits, set(combinations(sorted(set().union(NINES, FOURS), reverse=True), 2)))) - h99 - h44
h93o = set(filter(purge_suits, set(combinations(sorted(set().union(NINES, THREES), reverse=True), 2)))) - h99 - h33
h92o = set(filter(purge_suits, set(combinations(sorted(set().union(NINES, TWOS), reverse=True), 2)))) - h99 - h22


h87o = set(filter(purge_suits, set(combinations(sorted(set().union(EIGHTS, SEVENS), reverse=True), 2)))) - h88 - h77
h86o = set(filter(purge_suits, set(combinations(sorted(set().union(EIGHTS, SIXES), reverse=True), 2)))) - h88 - h66
h85o = set(filter(purge_suits, set(combinations(sorted(set().union(EIGHTS, FIVES), reverse=True), 2)))) - h88 - h55
h84o = set(filter(purge_suits, set(combinations(sorted(set().union(EIGHTS, FOURS), reverse=True), 2)))) - h88 - h44
h83o = set(filter(purge_suits, set(combinations(sorted(set().union(EIGHTS, THREES), reverse=True), 2)))) - h88 - h33
h82o = set(filter(purge_suits, set(combinations(sorted(set().union(EIGHTS, TWOS), reverse=True), 2)))) - h88 - h22


h76o = set(filter(purge_suits, set(combinations(sorted(set().union(SEVENS, SIXES), reverse=True), 2)))) - h77 - h66
h75o = set(filter(purge_suits, set(combinations(sorted(set().union(SEVENS, FIVES), reverse=True), 2)))) - h77 - h55
h74o = set(filter(purge_suits, set(combinations(sorted(set().union(SEVENS, FOURS), reverse=True), 2)))) - h77 - h44
h73o = set(filter(purge_suits, set(combinations(sorted(set().union(SEVENS, THREES), reverse=True), 2)))) - h77 - h33
h72o = set(filter(purge_suits, set(combinations(sorted(set().union(SEVENS, TWOS), reverse=True), 2)))) - h77 - h22


h65o = set(filter(purge_suits, set(combinations(sorted(set().union(SIXES, FIVES), reverse=True), 2)))) - h66 - h55
h64o = set(filter(purge_suits, set(combinations(sorted(set().union(SIXES, FOURS), reverse=True), 2)))) - h66 - h44
h63o = set(filter(purge_suits, set(combinations(sorted(set().union(SIXES, THREES), reverse=True), 2)))) - h66 - h33
h62o = set(filter(purge_suits, set(combinations(sorted(set().union(SIXES, TWOS), reverse=True), 2)))) - h66 - h22


h54o = set(filter(purge_suits, set(combinations(sorted(set().union(FIVES, FOURS), reverse=True), 2)))) - h55 - h44
h53o = set(filter(purge_suits, set(combinations(sorted(set().union(FIVES, THREES), reverse=True), 2)))) - h55 - h33
h52o = set(filter(purge_suits, set(combinations(sorted(set().union(FIVES, TWOS), reverse=True), 2)))) - h55 - h22


h43o = set(filter(purge_suits, set(combinations(sorted(set().union(FOURS, THREES), reverse=True), 2)))) - h44 - h33
h42o = set(filter(purge_suits, set(combinations(sorted(set().union(FOURS, TWOS), reverse=True), 2)))) - h44 - h22


h32o = set(filter(purge_suits, set(combinations(sorted(set().union(THREES, TWOS), reverse=True), 2)))) - h33 - h22


def hand_pick_range():
	""" blocks until user defines a range """
	current_selection = []
	ranks = 'AKQJT98765432'
	window = Tk()
	window.title("Range selector")
	window.geometry('330x400')
	buttons = {}
	for idx, rank in enumerate(ranks):
		lbl = Label(window, text=rank)
		lbl.grid(column=idx+1, row=0)
		lbl = Label(window, text=rank)
		lbl.grid(column=0, row=idx+1)


	def clicked(rank_1, rank_2, suited=False):
		_ranks = sorted([rank_1, rank_2], key=lambda x: ranks.index(x))
		var = 'h%s%s' % (_ranks[0], _ranks[1])

		if rank_1 != rank_2:
			var += 's' if suited else 'o'

		if var in current_selection:
			current_selection.remove(var)
		else:
			current_selection.append(var)
		buttons[rank_1][rank_2].configure(bg='red' if var in current_selection else 'white')
	

	def clear():
		current_selection.clear()
		for _buttons in buttons.values():
			for _button in _buttons.values():
				_button.configure(bg='white')


	def submit():
		if not current_selection:
			print('No range picked')
		window.destroy()


	for idx, rank_1 in enumerate(ranks):
		for idx_2, rank_2 in enumerate(ranks[:idx+1]):
			btn = Button(window, text="X", command=functools.partial(clicked, rank_1, rank_2, suited=False))
			btn.grid(column=idx_2+1, row=idx+1)
			btn.configure(bg='white')
			try:
				buttons[rank_1]
			except KeyError:
				 buttons[rank_1] = {}
			buttons[rank_1][rank_2] = btn

		for idx_2, rank_2 in enumerate(ranks[idx+1:]):
			btn = Button(window, text="Y", command=functools.partial(clicked, rank_1, rank_2, suited=True))
			btn.grid(column=idx+2+idx_2, row=idx+1)
			btn.configure(bg='white')
			try:
				buttons[rank_1]
			except KeyError:
				 buttons[rank_1] = {}
			buttons[rank_1][rank_2] = btn

	clear_button = Button(window, text="clear", command=clear)
	clear_button.grid(column=30, row=30)
	submit_button = Button(window, text="submit", command=submit)
	submit_button.grid(column=31, row=30)
	window.mainloop()
	return eval(' | '.join(current_selection))
