from itertools import combinations
from treys import Card, Deck, Evaluator
import random

def purge_offsuits(item):
	a, b = item
	return Card.get_suit_int(a) == Card.get_suit_int(b)

def purge_suits(item):
	a, b = item
	return Card.get_suit_int(a) != Card.get_suit_int(b)

def visualise_range(range):
	ranks = 'AKQJT98765432'
	print('  ' + ' '.join(ranks))

	for idx, rank_1 in enumerate(ranks):
		results = ''
		for rank_2 in ranks[:idx+1]:
			offsuited = (Card.new(rank_1 + 'd'), Card.new(rank_2 + 's'))
			_suited = (Card.new(rank_2 + 'd'), Card.new(rank_1 + 's'))
			if offsuited in range or _suited in range:
				results += 'X '
			else:
				results += '  '

		for rank_2 in ranks[idx+1:]:
			suited = (Card.new(rank_1 + 'd'), Card.new(rank_2 + 'd'))
			_suited = (Card.new(rank_2 + 'd'), Card.new(rank_1 + 'd'))
			if suited in range or _suited in range:
				results += 'X '
			else:
				results += '  '

			# offsuited = (Card.new(rank_1 + 'd'), Card.new(rank_2 + 'h'))
		print('%s %s' % (rank_1, results))


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

hA2s_plus = hAKs | hAQs | hAJs | hATs | hA9s | hA8s | hA7s | hA6s | hA5s | hA4s | hA3s | hA2s
hK9s_plus = hKQs | hKJs | hKTs | hK9s
hQTs_plus = hQJs | hQTs
hJ9s_plus = hJTs | hJ9s
hATo_plus = hAKo | hAQo | hAJo | hATo
hKJo_plus = hKQo | hKJo

h55_plus = hAA | hKK | hQQ | hJJ | hTT | h99 | h88 | h77 | h66 | h55
h22_plus = h55_plus | h44 | h33 | h22

# raise range, call range, raise size (pot ratio)

FULL_RANGE = hAA | hKK | hAKs | hAKo | hKQs | hAQs | hAJs | hKJs | hKTs | hATs | hA9s | hK9s | hK8s | hA8s | hA7s | hK7s | hK6s | hA6s | hA5s | hK5s | hK4s | hA4s | hA2s | hA3s | hK3s | hK2s | hQ2s | hQ3s | hQ5s | hQ4s | hQ8s | hQ9s | hAQo | hKQo | hQTs | hQJs | hQQ | hQ7s | hQ6s | hAJo | hA9o | hA8o | hA6o | hA5o | hA4o | hA3o | hA2o | hA7o | hATo | hKJo | hQ3o | hQ2o | hK9o | hK7o | hK6o | hK5o | hK4o | hK3o | hK2o | hK8o | hKTo | hQJo | hQ9o | hQ7o | hQ6o | hQ5o | hQ4o | hQTo | hQ8o | hJJ | hJ8o | hJ6o | hJ5o | hJ4o | hJ3o | hJTs | hTT | hT8o | hT6o | hT3o | hT2o | hJ9s | hT9s | h99 | h97o | h95o | h94o | h93o | h92o | hJ8s | hT8s | h87o | h85o | h84o | h83o | h82o | hJ7s | hT7s | h77 | h75o | h74o | h73o | h72o | hJ6s | hT6s | h96s | h86s | h76s | h66 | h65o | h64o | h63o | h62o | hJ5s | h95s | h85s | h75s | h55 | h52o | h53o | h54o | h65s | hT5s | hJ4s | h64s | h54s | h44 | h42o | h32o | h33 | h72s | h82s | h92s | hT2s | hJ2s | hJ3s | hT3s | h93s | h83s | h73s | h63s | h53s | h52s | h62s | h42s | h43s | h32s | h22 | h43o | hJ2o | hT4o | hT5o | h96o | h86o | h76o | hT7o | hJ7o | hJ9o | hT9o | hJTo | h98o | h88 | h98s | h87s | h97s | h74s | h84s | h94s | hT4s

# your position
OPEN_POSITION = [None for i in range(6)]
OPEN_POSITION[0] = (hA2s_plus | hK9s_plus | hQTs_plus | hJ9s_plus | hT9s | h55_plus | hATo_plus | hKJo_plus, 0.5)
OPEN_POSITION[1] = (OPEN_POSITION[0][0] | hKTo | hQ9s | h44 | hQJo, {}, 0.5)
OPEN_POSITION[2] = (OPEN_POSITION[1][0] | hK8s | hK7s | hK6s | hQ8s | hT8s | h98s | h97s | h87s | h76s | h65s | h54s | h33 | h22 | hA9o | hQTo | hJTo, {}, 0.5)
OPEN_POSITION[3] = (OPEN_POSITION[2][0] | hK5s | hK4s | hK3s | hK2s | hQ7s | hQ6s | hQ5s | hJ8s | hJ7s | hT7s | h96s | h86s | h85s | h75s | h64s | hA8o | hA7o | hA6o | hA5o | hA4o | hK9o | hQ9o | hJ9o | hT9o, {}, 0.5)
OPEN_POSITION[4] = ((OPEN_POSITION[3][0] | hQ2s | h53s | hK5o | h98o | h87o | h76o) - hA6s - hA2s - hK7s - hK6s - hK5s - hK4s - hK3s - hK2s - hQ9s - hQ6s - hQ5s - hJ8s - hT8s - hT7s - h96s - h87s - h86s - h85s - h76s - h75s - h64s - hAJo - hATo - hA8o - hA6o - hA5o - hA4o - hKTo - hKJo - hQJo - hQTo - hQ9o - hJTo - hQQ - hJJ - h44, hA6s | hA2s | hK7s | hK6s | hK5s | hK4s | hK3s | hK2s | hQ9s | hQ6s | hQ5s | hQ4s | hQ3s | hJ8s | hJ6s | hJ5s | hJ4s | hJ3s | hJ2s | hT8s | hT7s | hT6s | hT5s | hT4s | h96s | h95s | h87s | h86s | h85s | h76s | h75s | h74s | h64s | h63s | h43s | hQQ | hJJ | h44 | hAJo | hATo | hA8o | hA6o | hA5o | hA4o | hA3o | hA2o | hKJo | hKTo | hK8o | hK7o | hK4o | hQJo | hQTo | hQ9o | hQ8o | hQ7o | hJTo | hJ8o | hJ7o | hT8o | hT7o | h97o | h65o | hK6o, 1)
OPEN_POSITION[5] = (OPEN_POSITION[4][0], OPEN_POSITION[4][1], 1)

# your position, raiser position
FACING_RAISE = [[None for i in range(6)] for i in range(6)]
FACING_RAISE[1][0] = (hAA | hAKo | hKK | hAKs | hKQs | hQQ | hAJs | hATs | hJJ | h76s | h65s | hA5s | hA4s | hA3s | hA2s, hAQs | hTT | h99, 1)
FACING_RAISE[2][0] = (hAA | hAKo | hKK | hAKs | hKQs | hQQ | hAJs | hATs | hA5s | hA4s | hA3s | hA2s | h65s, hAQs | hKJs | hAQo | hJJ | hTT | h99 | h88, 1)
FACING_RAISE[2][1] = (hAA | hAKo | hKK | hAKs | hKQs | hQQ | hAQo | hAJs | hATs | h65s | h76s | hA5s | hA4s | hA3s | hA2s, hAQs | hKJs | hQJs | hJJ | hTT | h99 | h88, 1)
FACING_RAISE[3][0] = (hAA | hAKo | hKK | hAKs | hKQs | hQQ | hKJs | hAJs | hATs | hA5s | hA4s | hA3s | hA2s | h76s | h65s | h54s, hAQs | hAQo | hQJs | hJJ | hJTs | hTT | h99 | h88 | h77, 1)
FACING_RAISE[3][1] = (hAA | hAKo | hKK | hAKs | hAQs | hKQs | hQQ | hKJs | hJJ | hATs | hA9s | h76s | h65s | h54s | hA5s | hA4s | hA3s | hA2s, hAQo | hAJs | hQJs | hJTs | hTT | h99 | h88 | h77 | h76s | h65s | h54s, 1)
FACING_RAISE[3][2] = (hAA | hAKo | hKK | hAKs | hAQs | hKQs | hKJs | hQQ | hKQo | hAJo | hATs | hA9s | hA8s | hA5s | hA4s | hA3s | hA2s | h76s | h65s | h54s, hAJs | hKTs | hAQo | hQJs | hJTs | hTT | h99 | h88 | h77, 1)
FACING_RAISE[4][0] = (hAQo | hAKo | hAA | hKK | hAKs | hAQs | hKQs | hQQ | hKJs | hQJs | hJJ | hTT | hAJs | hATs | hA5s | hA4s,  h99 | h88 | h77, 1)
FACING_RAISE[4][1] = (hAA | hAKs | hAQs | hAJs | hATs | hAKo | hKK | hKQs | hKJs | hAQo | hQQ | hQJs | hJJ | hJTs | hTT | h99 | h88 | hA5s | hA4s,  h77 | h66, 1)
FACING_RAISE[4][2] = (hAA | hAKs | hAQs | hAJs | hATs | hA9s | hA5s | hA4s | hAKo | hKK | hKQs | hKJs | hKTs | hAQo | hKQo | hQQ | hQJs | hQTs | hAJo | hJJ | hJTs | hTT | hT9s | h99 | h88 | h77 | h66 | h55, {}, 1)
FACING_RAISE[4][3] = (hAA | hAKs | hAQs | hAJs | hATs | hA9s | hA8s | hA7s | hA5s | hA4s | hAKo | hKK | hKQs | hKJs | hKTs | hK9s | hAQo | hKQo | hQQ | hQJs | hQTs | hQ9s | hJ9s | hJTs | hJJ | hQJo | hAJo | hTT | hT9s | h99 | h88 | h77 | h66 | h55, {}, 1)
FACING_RAISE[5][0] = (hAA | hAKs | hKK | hAQs | hQQ, hAJs | hATs | hA9s | hA8s | hA7s | hA6s | hA5s | hA4s | hA3s | hA2s | hAKo | hKQs | hKJs | hK9s | hKTs | hAQo | hKQo | hQJs | hQTs | hQ9s | hAJo | hATo | hJJ | hJTs | hJ9s | hTT | hT9s | hT8s | h99 | h98s | h88 | h87s | h86s | h77 | h76s | h75s | h66 | h65s | h64s | h55 | h54s | h53s | h44 | h33 | h22, 1)
FACING_RAISE[5][1] = (hAA | hAKo | hKK | hAKs | hAQs | hKQs | hAJs | hQQ | hJJ | hTT, hATs | hA9s | hA8s | hA7s | hA6s | hA5s | hA4s | hA3s | hA2s | hAKo | hKJs | hK9s | hKTs | hAQo | hKQo | hQTs | hQ9s | hAJo | hATo | hJTs | hJ9s | hT9s | hT8s | h99 | h98s | h88 | h87s | h86s | h77 | h76s | h75s | h66 | h65s | h64s | h55 | h54s | h53s | h44 | h33 | h22 | h97s | hK8s | hK7s | hKJo | hQJo, 1)
FACING_RAISE[5][2] = (hAA | hAKs | hAQs | hAJs | hATs | hAKo | hKK | hKQs | hQQ | hQJs | hJJ | hJTs | hTT, hA9s | hA8s | hA7s | hA6s | hA5s | hA4s | hA3s | hA2s | hKJs | hKTs | hK9s | hK8s | hK7s | hK6s | hK4s | hAQo | hKQo | hQTs | hQ9s | hQ8s | hAJo | hKJo | hQJo | hJ9s | hJ8s | hATo | hKTo | hJTo | hT9s | hT8s | hT7s | h99 | h98s | h97s | h88 | h87s | h86s | h77 | h76s | h75s | h66 | h65s | h64s | h55 | h54s | h53s | h44 | h43s | h33 | h22, 1)
FACING_RAISE[5][3] = (hAA | hAKo | hKK | hAKs | hAQs | hKQs | hKJs | hAJs | hATs | hA7s | hA5s | hA4s | hA3s | hAQo | hKQo | hQQ | hQJs | hJJ | hJTs | hTT | hT9s | h88 | h77 | h66, hA9s | hA8s | hA6s | hA2s | hKTs | hK9s | hK8s | hK7s | hK6s | hK5s | hK4s | hK3s | hK2s | hQTs | hQ9s | hQ8s | hQ7s | hQ6s | hAJo | hKJo | hQJo | hJ9s | hJ8s | hJ7s | hATo | hA9o | hA8o | hKTo | hQTo | hJTo | hT8s | hT7s | h97s | h96s | h98s | h99 | hT9o | h87s | h86s | h76s | h75s | h65s | h64s | h65o | h55 | h54s | h44 | h43s | h33 | h22, 1)
FACING_RAISE[5][4] = (hAA | hAKs | hAQs | hAJs | hA2s | hK2s | hK3s | hAKo | hKK | hKQs | hKJs | hKTs | hK9s | hAQo | hKQo | hQQ | hQJs | hQTs | hQ8s | hAJo | hJJ | hJTs | hJ9s | hTT | h99 | hA4o | hA3o | hA2o, hATs | hA9s | hA8s | hA7s | hA6s | hA5s | hA4s | hA3s | hK8s | hK7s | hK6s | hK5s | hK4s | hQ9s | hQ7s | hQ6s | hQ5s | hQ4s | hQ3s | hQ2s | hKJo | hQJo | hJ8s | hJ7s | hJ6s | hJ5s | hJ4s | hJ3s | hJ2s | hATo | hKTo | hQTo | hJTo | hT9s | hT8s | hT7s | hT6s | hT5s | hT4s | hT3s | hT2s | hA9o | hK9o | hQ9o | hJ9o | hT9o | h98s | h97s | h96s | h95s | h94s | h93s | h92s | hA8o | hK8o | hQ8o | hJ8o | hT8o | h98o | h88 | h87s | h86s | h85s | h84s | h83s | h82s | hA7o | hK7o | hQ7o | hT7o | h97o | h87o | h77 | h76s | h75s | h74s | h73s  | hA6o | hA5o | h86o | h76o | h66 | h65s | h64s | h63s | h62s | h52s | h53s | h54s | h55 | h65o | h54o | h44 | h43s | h42s | h32s | h33 | h22, 1)

# you called bb and someone after you raised
FACING_RAISE[4][5] = (hAA | hAKs | hAQs | hAJs | hKK | hAKo | hAQo | hKQo | hQJs | hQQ | hJJ | hT9s | h98s | h87s, hATs | hA9s | hA8s | hA7s | hA5s | hA6s | hA3s | hA4s | hA2s | hKQs | hKJs | hK9s | hKTs | hK8s | hK6s | hK7s | hK5s | hK4s | hK2s | hK3s | hQ3s | hQ5s | hQ6s | hQ7s | hQ8s | hQTs | hQ9s | hAJo | hKJo | hQJo | hJTs | hJ9s | hJ8s | hJ7s | hJ6s | hJ5s | hT6s | hT7s | hT8s | hTT | hJTo | hQTo | hKTo | hATo | hA9o | hA8o | hK9o | hQ9o | hJ9o | hT9o | h99 | h97s | h95s | h96s | h85s | h88 | h86s | h98o | hA7o | hA6o | hA5o | hA4o | h77 | h76s | h75s | h74s | h66 | h65s | h64s | h63s | h55 | h54s | h53s | h52s | h44 | h43s | h42s | h33 | h32s | h22, 1)
FACING_RAISE[3][4] = (hAA | hAKs | hAQs | hAJs | hKK | hAKo | hAQo | hKQo | hQJs | hQQ | hJJ | hT9s | h98s | h87s, hATs | hA9s | hA8s | hA7s | hA5s | hA6s | hA3s | hA4s | hA2s | hKQs | hKJs | hK9s | hKTs | hK8s | hK6s | hK7s | hK5s | hK4s | hK2s | hK3s | hQ3s | hQ5s | hQ6s | hQ7s | hQ8s | hQTs | hQ9s | hAJo | hKJo | hQJo | hJTs | hJ9s | hJ8s | hJ7s | hJ6s | hJ5s | hT6s | hT7s | hT8s | hTT | hJTo | hQTo | hKTo | hATo | hA9o | hA8o | hK9o | hQ9o | hJ9o | hT9o | h99 | h97s | h95s | h96s | h85s | h88 | h86s | h98o | hA7o | hA6o | hA5o | hA4o | h77 | h76s | h75s | h74s | h66 | h65s | h64s | h63s | h55 | h54s | h53s | h52s | h44 | h43s | h42s | h33 | h32s | h22, 1)
FACING_RAISE[3][5] = (hAA | hAKs | hAQs | hAJs | hKK | hAKo | hAQo | hKQo | hQJs | hQQ | hJJ | hT9s | h98s | h87s, hATs | hA9s | hA8s | hA7s | hA5s | hA6s | hA3s | hA4s | hA2s | hKQs | hKJs | hK9s | hKTs | hK8s | hK6s | hK7s | hK5s | hK4s | hK2s | hK3s | hQ3s | hQ5s | hQ6s | hQ7s | hQ8s | hQTs | hQ9s | hAJo | hKJo | hQJo | hJTs | hJ9s | hJ8s | hJ7s | hJ6s | hJ5s | hT6s | hT7s | hT8s | hTT | hJTo | hQTo | hKTo | hATo | hA9o | hA8o | hK9o | hQ9o | hJ9o | hT9o | h99 | h97s | h95s | h96s | h85s | h88 | h86s | h98o | hA7o | hA6o | hA5o | hA4o | h77 | h76s | h75s | h74s | h66 | h65s | h64s | h63s | h55 | h54s | h53s | h52s | h44 | h43s | h42s | h33 | h32s | h22, 1)
FACING_RAISE[2][3] = (hAA | hAKs | hAQs | hAJs | hKK | hAKo | hAQo | hKQo | hQJs | hQQ | hJJ | hT9s | h98s | h87s, hATs | hA9s | hA8s | hA7s | hA5s | hA6s | hA3s | hA4s | hA2s | hKQs | hKJs | hK9s | hKTs | hK8s | hK6s | hK7s | hK5s | hK4s | hK2s | hK3s | hQ3s | hQ5s | hQ6s | hQ7s | hQ8s | hQTs | hQ9s | hAJo | hKJo | hQJo | hJTs | hJ9s | hJ8s | hJ7s | hJ6s | hJ5s | hT6s | hT7s | hT8s | hTT | hJTo | hQTo | hKTo | hATo | hA9o | hA8o | hK9o | hQ9o | hJ9o | hT9o | h99 | h97s | h95s | h96s | h85s | h88 | h86s | h98o | hA7o | hA6o | hA5o | hA4o | h77 | h76s | h75s | h74s | h66 | h65s | h64s | h63s | h55 | h54s | h53s | h52s | h44 | h43s | h42s | h33 | h32s | h22, 1)
FACING_RAISE[2][4] = (hAA | hAKs | hAQs | hAJs | hKK | hAKo | hAQo | hKQo | hQJs | hQQ | hJJ | hT9s | h98s | h87s, hATs | hA9s | hA8s | hA7s | hA5s | hA6s | hA3s | hA4s | hA2s | hKQs | hKJs | hK9s | hKTs | hK8s | hK6s | hK7s | hK5s | hK4s | hK2s | hK3s | hQ3s | hQ5s | hQ6s | hQ7s | hQ8s | hQTs | hQ9s | hAJo | hKJo | hQJo | hJTs | hJ9s | hJ8s | hJ7s | hJ6s | hJ5s | hT6s | hT7s | hT8s | hTT | hJTo | hQTo | hKTo | hATo | hA9o | hA8o | hK9o | hQ9o | hJ9o | hT9o | h99 | h97s | h95s | h96s | h85s | h88 | h86s | h98o | hA7o | hA6o | hA5o | hA4o | h77 | h76s | h75s | h74s | h66 | h65s | h64s | h63s | h55 | h54s | h53s | h52s | h44 | h43s | h42s | h33 | h32s | h22, 1)
FACING_RAISE[2][5] = (hAA | hAKs | hAQs | hAJs | hKK | hAKo | hAQo | hKQo | hQJs | hQQ | hJJ | hT9s | h98s | h87s, hATs | hA9s | hA8s | hA7s | hA5s | hA6s | hA3s | hA4s | hA2s | hKQs | hKJs | hK9s | hKTs | hK8s | hK6s | hK7s | hK5s | hK4s | hK2s | hK3s | hQ3s | hQ5s | hQ6s | hQ7s | hQ8s | hQTs | hQ9s | hAJo | hKJo | hQJo | hJTs | hJ9s | hJ8s | hJ7s | hJ6s | hJ5s | hT6s | hT7s | hT8s | hTT | hJTo | hQTo | hKTo | hATo | hA9o | hA8o | hK9o | hQ9o | hJ9o | hT9o | h99 | h97s | h95s | h96s | h85s | h88 | h86s | h98o | hA7o | hA6o | hA5o | hA4o | h77 | h76s | h75s | h74s | h66 | h65s | h64s | h63s | h55 | h54s | h53s | h52s | h44 | h43s | h42s | h33 | h32s | h22, 1)
FACING_RAISE[1][2] = (hAA | hAKs | hAQs | hAJs | hKK | hAKo | hAQo | hKQo | hQJs | hQQ | hJJ | hT9s | h98s | h87s, hATs | hA9s | hA8s | hA7s | hA5s | hA6s | hA3s | hA4s | hA2s | hKQs | hKJs | hK9s | hKTs | hK8s | hK6s | hK7s | hK5s | hK4s | hK2s | hK3s | hQ3s | hQ5s | hQ6s | hQ7s | hQ8s | hQTs | hQ9s | hAJo | hKJo | hQJo | hJTs | hJ9s | hJ8s | hJ7s | hJ6s | hJ5s | hT6s | hT7s | hT8s | hTT | hJTo | hQTo | hKTo | hATo | hA9o | hA8o | hK9o | hQ9o | hJ9o | hT9o | h99 | h97s | h95s | h96s | h85s | h88 | h86s | h98o | hA7o | hA6o | hA5o | hA4o | h77 | h76s | h75s | h74s | h66 | h65s | h64s | h63s | h55 | h54s | h53s | h52s | h44 | h43s | h42s | h33 | h32s | h22, 1)
FACING_RAISE[1][3] = (hAA | hAKs | hAQs | hAJs | hKK | hAKo | hAQo | hKQo | hQJs | hQQ | hJJ | hT9s | h98s | h87s, hATs | hA9s | hA8s | hA7s | hA5s | hA6s | hA3s | hA4s | hA2s | hKQs | hKJs | hK9s | hKTs | hK8s | hK6s | hK7s | hK5s | hK4s | hK2s | hK3s | hQ3s | hQ5s | hQ6s | hQ7s | hQ8s | hQTs | hQ9s | hAJo | hKJo | hQJo | hJTs | hJ9s | hJ8s | hJ7s | hJ6s | hJ5s | hT6s | hT7s | hT8s | hTT | hJTo | hQTo | hKTo | hATo | hA9o | hA8o | hK9o | hQ9o | hJ9o | hT9o | h99 | h97s | h95s | h96s | h85s | h88 | h86s | h98o | hA7o | hA6o | hA5o | hA4o | h77 | h76s | h75s | h74s | h66 | h65s | h64s | h63s | h55 | h54s | h53s | h52s | h44 | h43s | h42s | h33 | h32s | h22, 1)
FACING_RAISE[1][4] = (hAA | hAKs | hAQs | hAJs | hKK | hAKo | hAQo | hKQo | hQJs | hQQ | hJJ | hT9s | h98s | h87s, hATs | hA9s | hA8s | hA7s | hA5s | hA6s | hA3s | hA4s | hA2s | hKQs | hKJs | hK9s | hKTs | hK8s | hK6s | hK7s | hK5s | hK4s | hK2s | hK3s | hQ3s | hQ5s | hQ6s | hQ7s | hQ8s | hQTs | hQ9s | hAJo | hKJo | hQJo | hJTs | hJ9s | hJ8s | hJ7s | hJ6s | hJ5s | hT6s | hT7s | hT8s | hTT | hJTo | hQTo | hKTo | hATo | hA9o | hA8o | hK9o | hQ9o | hJ9o | hT9o | h99 | h97s | h95s | h96s | h85s | h88 | h86s | h98o | hA7o | hA6o | hA5o | hA4o | h77 | h76s | h75s | h74s | h66 | h65s | h64s | h63s | h55 | h54s | h53s | h52s | h44 | h43s | h42s | h33 | h32s | h22, 1)
FACING_RAISE[1][5] = (hAA | hAKs | hAQs | hAJs | hKK | hAKo | hAQo | hKQo | hQJs | hQQ | hJJ | hT9s | h98s | h87s, hATs | hA9s | hA8s | hA7s | hA5s | hA6s | hA3s | hA4s | hA2s | hKQs | hKJs | hK9s | hKTs | hK8s | hK6s | hK7s | hK5s | hK4s | hK2s | hK3s | hQ3s | hQ5s | hQ6s | hQ7s | hQ8s | hQTs | hQ9s | hAJo | hKJo | hQJo | hJTs | hJ9s | hJ8s | hJ7s | hJ6s | hJ5s | hT6s | hT7s | hT8s | hTT | hJTo | hQTo | hKTo | hATo | hA9o | hA8o | hK9o | hQ9o | hJ9o | hT9o | h99 | h97s | h95s | h96s | h85s | h88 | h86s | h98o | hA7o | hA6o | hA5o | hA4o | h77 | h76s | h75s | h74s | h66 | h65s | h64s | h63s | h55 | h54s | h53s | h52s | h44 | h43s | h42s | h33 | h32s | h22, 1)


# 1st raiser position, last raiser position
FACING_3B = [[None for i in range(6)] for i in range(6)]
FACING_3B[0][1] = (hAA | hAKs | hKK | hAKo | hQQ, hAQs | hKQs | hAJs | hJJ | hTT | h99 | h88, 1)
FACING_3B[0][2] = (hAA | hAKo | hKK | hAKs | hQQ, hAJs | hAQs | hJJ | hTT | h99 | h88, 1)
FACING_3B[0][3] = (hAA | hAKo | hKK | hAKs | hQQ, hAQs | hKQs | hAJs | hATs | hJJ | hTT | h99 | h88 | h77, 1)
FACING_3B[0][4] = (hAA | hAKs | hA3s | hA2s, hAQs | hAJs | hATs | hAKo | hKK | hKQs | hQQ | hJJ | hJTs | hTT | hT9s | h99 | h88 | h87s | h77 | h76s | h66 | h65s | h55 | h54s | h64s | h53s, 1)
FACING_3B[0][5] = (hAA | hA2s, hAKs | hAQs | hAJs | hATs | hA5s | hA4s | hA3s | hAKo | hKK | hKQs | hKJs | hKTs | hQQ | hQJs | hQTs | hJJ | hJTs | hJ9s | hTT | hT9s | hT8s | h99 | h98s | h88 | h87s | h86s | h77 | h76s | h75s | h66 | h65s | h64s | h55 | h54s | h53s | h44 | h43s | h33 | h22, 1)

FACING_3B[1][2] = (hAA | hAKo | hKK | hAKs | hKQs | hQQ | hATs | hJJ | hA5s | hA4s, hAQs | hAJs | hJTs | hTT | h99 | h88 | h77, 1)
FACING_3B[1][3] = (hAA | hAKo | hKK | hAKs | hKQs | hQQ | hJJ | hTT | hA4s, hAQs | hAJs | hATs | hJTs | h99 | h88 | h77 | h66, 1)
FACING_3B[1][4] = (hAA | hAKs | hA2s | hA3s, hAQs | hAJs | hATs | hA5s | hA4s | hAKo | hKK | hKQs | hKJs | hQQ | hQJs | hJJ | hJTs | hTT | hT9s | h99 | h88 | h87s | h77 | h76s | h66 | h65s | h64s | h55 | h54s | h54s | h53s, 1)
FACING_3B[1][5] = (hAA | hA2s, hAQs | hAJs | hATs | hA5s | hA4s | hAKo | hKK | hKQs | hKJs | hQQ | hQJs | hJJ | hJTs | hTT | hT9s | h99 | h88 | h87s | h77 | h76s | h66 | h65s | h64s | h55 | h54s | h54s | h53s | hAKs | hA9s | hA3s | hKTs | hQTs | hJ9s | hT8s | h98s | h75s | h44 | h43s | h33 | h22, 1)
FACING_3B[1][0] = (hAA | hA2s, hAQs | hAJs | hATs | hA5s | hA4s | hAKo | hKK | hKQs | hKJs | hQQ | hQJs | hJJ | hJTs | hTT | hT9s | h99 | h88 | h87s | h77 | h76s | h66 | h65s | h64s | h55 | h54s | h54s | h53s | hAKs | hA9s | hA3s | hKTs | hQTs | hJ9s | hT8s | h98s | h75s | h44 | h43s | h33 | h22, 1)

FACING_3B[2][3] = (hAA | hAKs | hA3s | hA2s | hAKo | hKK | hKQs | hQQ | hJJ | hTT, hAQs | hAJs | hATs | hKJs | hQJs | hAQo | hJTs | hT9s | h99 | h88 | h77 | h66, 1)
FACING_3B[2][4] = (hAA | hAKo | hKK | hAKs, hAQs | hAJs | hATs | hA5s | hA4s | hKQs | hKJs | hQQ | hQJs | hJJ | hJTs | hTT | hT9s | h99 | h88 | h87s | h77 | h76s | h66 | h65s | h64s | h55 | h54s | h54s | h53s | hA9s | hA3s | hKTs | hQTs | hJ9s | hT8s | h98s | h75s | h44 | h33 | h22 | hA8s | hA7s | hA6s | hA2s | hAQo | h86s, 1)
FACING_3B[2][5] = (hAA | hAKs, hAQs | hAJs | hATs | hA5s | hA4s | hAKo | hKK | hKQs | hKJs | hQQ | hQJs | hJJ | hJTs | hTT | hT9s | h99 | h88 | h87s | h77 | h76s | h66 | h65s | h64s | h55 | h54s | h54s | h53s | hA9s | hA3s | hKTs | hQTs | hJ9s | hT8s | h98s | h75s | h44 | h33 | h22 | hA8s | hA7s | hA6s | hA2s | hAQo | h86s | hK9s | hQ9s | h97s | h43s, 1)
FACING_3B[2][1] = (hAA | hAKs, hAQs | hAJs | hATs | hA5s | hA4s | hAKo | hKK | hKQs | hKJs | hQQ | hQJs | hJJ | hJTs | hTT | hT9s | h99 | h88 | h87s | h77 | h76s | h66 | h65s | h64s | h55 | h54s | h54s | h53s | hA9s | hA3s | hKTs | hQTs | hJ9s | hT8s | h98s | h75s | h44 | h33 | h22 | hA8s | hA7s | hA6s | hA2s | hAQo | h86s | hK9s | hQ9s | h97s | h43s, 1)
FACING_3B[2][0] = (hAA | hAKs, hAQs | hAJs | hATs | hA5s | hA4s | hAKo | hKK | hKQs | hKJs | hQQ | hQJs | hJJ | hJTs | hTT | hT9s | h99 | h88 | h87s | h77 | h76s | h66 | h65s | h64s | h55 | h54s | h54s | h53s | hA9s | hA3s | hKTs | hQTs | hJ9s | hT8s | h98s | h75s | h44 | h33 | h22 | hA8s | hA7s | hA6s | hA2s | hAQo | h86s | hK9s | hQ9s | h97s | h43s, 1)

FACING_3B[3][4] = (hKK | hAKs | hAA | hAKo | hK2s | hQQ | hJJ, hAQs | hAJs | hATs | hA5s | hA4s | hKQs | hKJs | hQJs | hJTs | hTT | hT9s | h99 | h88 | h87s | h77 | h76s | h66 | h65s | h64s | h55 | h54s | h54s | h53s | hA9s | hA3s | hKTs | hQTs | hJ9s | hT8s | h98s | h75s | h44 | h33 | h22 | hA8s | hA7s | hA6s | hA2s | hAQo | h86s | hK9s | hQ9s | h97s | h43s | hKQo | hAJo | hK8s | hK7s | hK6s | hJ8s, 1)
FACING_3B[3][5] = (hAKo | hKK | hAKs | hAA | h85s, hAQs | hAJs | hATs | hA5s | hA4s | hKQs | hKJs | hQJs | hJTs | hTT | hT9s | h99 | h88 | h87s | h77 | h76s | h66 | h65s | h64s | h55 | h54s | h54s | h53s | hA9s | hA3s | hKTs | hQTs | hJ9s | hT8s | h98s | h75s | h44 | h33 | h22 | hA8s | hA7s | hA6s | hA2s | hAQo | h86s | hK9s | hQ9s | h97s | h43s | hKQo | hAJo | hK8s | hK7s | hK6s | hJ8s | hQQ | hJJ | hKJo | hATo | hT7s | hQJo, 1)
FACING_3B[3][2] = (hAKo | hKK | hAKs | hAA | h85s, hAQs | hAJs | hATs | hA5s | hA4s | hKQs | hKJs | hQJs | hJTs | hTT | hT9s | h99 | h88 | h87s | h77 | h76s | h66 | h65s | h64s | h55 | h54s | h54s | h53s | hA9s | hA3s | hKTs | hQTs | hJ9s | hT8s | h98s | h75s | h44 | h33 | h22 | hA8s | hA7s | hA6s | hA2s | hAQo | h86s | hK9s | hQ9s | h97s | h43s | hKQo | hAJo | hK8s | hK7s | hK6s | hJ8s | hQQ | hJJ | hKJo | hATo | hT7s | hQJo, 1)
FACING_3B[3][1] = (hAKo | hKK | hAKs | hAA | h85s, hAQs | hAJs | hATs | hA5s | hA4s | hKQs | hKJs | hQJs | hJTs | hTT | hT9s | h99 | h88 | h87s | h77 | h76s | h66 | h65s | h64s | h55 | h54s | h54s | h53s | hA9s | hA3s | hKTs | hQTs | hJ9s | hT8s | h98s | h75s | h44 | h33 | h22 | hA8s | hA7s | hA6s | hA2s | hAQo | h86s | hK9s | hQ9s | h97s | h43s | hKQo | hAJo | hK8s | hK7s | hK6s | hJ8s | hQQ | hJJ | hKJo | hATo | hT7s | hQJo, 1)
FACING_3B[3][0] = (hAKo | hKK | hAKs | hAA | h85s, hAQs | hAJs | hATs | hA5s | hA4s | hKQs | hKJs | hQJs | hJTs | hTT | hT9s | h99 | h88 | h87s | h77 | h76s | h66 | h65s | h64s | h55 | h54s | h54s | h53s | hA9s | hA3s | hKTs | hQTs | hJ9s | hT8s | h98s | h75s | h44 | h33 | h22 | hA8s | hA7s | hA6s | hA2s | hAQo | h86s | hK9s | hQ9s | h97s | h43s | hKQo | hAJo | hK8s | hK7s | hK6s | hJ8s | hQQ | hJJ | hKJo | hATo | hT7s | hQJo, 1)

FACING_3B[4][5] = (hAA | hAKs | hAQs | hA3s | hA2s | hAKo | hKK | hAQo | hQQ | hAJo | hATo, hAJs | hATs | hA9s | hA8s | hA7s | hA6s | hA5s | hA4s | hKQs | hKJs | hKTs | hK9s | hQJs | hQTs | hQ9s | hJJ | hJTs | hJ9s | hTT | hT9s | hT8s | h99 | h98s | h88 | h87s | h77 | h76s | h66 | h65s | h55 | h54s | h44 | h33 | h22 | hKQo | hKJo | hQJo, 1)
FACING_3B[4][3] = (hAA | hAKs | hAQs | hA3s | hA2s | hAKo | hKK | hAQo | hQQ | hAJo | hATo, hAJs | hATs | hA9s | hA8s | hA7s | hA6s | hA5s | hA4s | hKQs | hKJs | hKTs | hK9s | hQJs | hQTs | hQ9s | hJJ | hJTs | hJ9s | hTT | hT9s | hT8s | h99 | h98s | h88 | h87s | h77 | h76s | h66 | h65s | h55 | h54s | h44 | h33 | h22 | hKQo | hKJo | hQJo, 1)
FACING_3B[4][2] = (hAA | hAKs | hAQs | hA3s | hA2s | hAKo | hKK | hAQo | hQQ | hAJo | hATo, hAJs | hATs | hA9s | hA8s | hA7s | hA6s | hA5s | hA4s | hKQs | hKJs | hKTs | hK9s | hQJs | hQTs | hQ9s | hJJ | hJTs | hJ9s | hTT | hT9s | hT8s | h99 | h98s | h88 | h87s | h77 | h76s | h66 | h65s | h55 | h54s | h44 | h33 | h22 | hKQo | hKJo | hQJo, 1)
FACING_3B[4][1] = (hAA | hAKs | hAQs | hA3s | hA2s | hAKo | hKK | hAQo | hQQ | hAJo | hATo, hAJs | hATs | hA9s | hA8s | hA7s | hA6s | hA5s | hA4s | hKQs | hKJs | hKTs | hK9s | hQJs | hQTs | hQ9s | hJJ | hJTs | hJ9s | hTT | hT9s | hT8s | h99 | h98s | h88 | h87s | h77 | h76s | h66 | h65s | h55 | h54s | h44 | h33 | h22 | hKQo | hKJo | hQJo, 1)
FACING_3B[4][0] = (hAA | hAKs | hAQs | hA3s | hA2s | hAKo | hKK | hAQo | hQQ | hAJo | hATo, hAJs | hATs | hA9s | hA8s | hA7s | hA6s | hA5s | hA4s | hKQs | hKJs | hKTs | hK9s | hQJs | hQTs | hQ9s | hJJ | hJTs | hJ9s | hTT | hT9s | hT8s | h99 | h98s | h88 | h87s | h77 | h76s | h66 | h65s | h55 | h54s | h44 | h33 | h22 | hKQo | hKJo | hQJo, 1)

FACING_3B[5][0] = (hAA | hAKs | hAQs | hA3s | hA2s | hAKo | hKK | hAQo | hQQ | hAJo | hATo, hAJs | hATs | hA9s | hA8s | hA7s | hA6s | hA5s | hA4s | hKQs | hKJs | hKTs | hK9s | hQJs | hQTs | hQ9s | hJJ | hJTs | hJ9s | hTT | hT9s | hT8s | h99 | h98s | h88 | h87s | h77 | h76s | h66 | h65s | h55 | h54s | h44 | h33 | h22 | hKQo | hKJo | hQJo, 1)
FACING_3B[5][1] = (hAA | hAKs | hAQs | hA3s | hA2s | hAKo | hKK | hAQo | hQQ | hAJo | hATo, hAJs | hATs | hA9s | hA8s | hA7s | hA6s | hA5s | hA4s | hKQs | hKJs | hKTs | hK9s | hQJs | hQTs | hQ9s | hJJ | hJTs | hJ9s | hTT | hT9s | hT8s | h99 | h98s | h88 | h87s | h77 | h76s | h66 | h65s | h55 | h54s | h44 | h33 | h22 | hKQo | hKJo | hQJo, 1)
FACING_3B[5][2] = (hAA | hAKs | hAQs | hA3s | hA2s | hAKo | hKK | hAQo | hQQ | hAJo | hATo, hAJs | hATs | hA9s | hA8s | hA7s | hA6s | hA5s | hA4s | hKQs | hKJs | hKTs | hK9s | hQJs | hQTs | hQ9s | hJJ | hJTs | hJ9s | hTT | hT9s | hT8s | h99 | h98s | h88 | h87s | h77 | h76s | h66 | h65s | h55 | h54s | h44 | h33 | h22 | hKQo | hKJo | hQJo, 1)
FACING_3B[5][3] = (hAA | hAKs | hAQs | hA3s | hA2s | hAKo | hKK | hAQo | hQQ | hAJo | hATo, hAJs | hATs | hA9s | hA8s | hA7s | hA6s | hA5s | hA4s | hKQs | hKJs | hKTs | hK9s | hQJs | hQTs | hQ9s | hJJ | hJTs | hJ9s | hTT | hT9s | hT8s | h99 | h98s | h88 | h87s | h77 | h76s | h66 | h65s | h55 | h54s | h44 | h33 | h22 | hKQo | hKJo | hQJo, 1)
FACING_3B[5][4] = (hAA | hAKs | hAQs | hA3s | hA2s | hAKo | hKK | hAQo | hQQ | hAJo | hATo, hAJs | hATs | hA9s | hA8s | hA7s | hA6s | hA5s | hA4s | hKQs | hKJs | hKTs | hK9s | hQJs | hQTs | hQ9s | hJJ | hJTs | hJ9s | hTT | hT9s | hT8s | h99 | h98s | h88 | h87s | h77 | h76s | h66 | h65s | h55 | h54s | h44 | h33 | h22 | hKQo | hKJo | hQJo, 1)


# 2nd raiser position, 3rd raiser position
FACING_4B = [[None for i in range(6)] for i in range(6)]
FACING_4B[1][0] = (hAA, hAKs | hAQs | hAJs | hATs | hAKo | hKK | hQQ | hJJ | hTT | h88 | h77 | h66, 0.5)
FACING_4B[2][0] = (hAA, hAKo | hKK | hAKs | hAQs | hAJs | hQQ | hJJ, 0.5)
FACING_4B[2][1] = (hAA | hAKs, hAKo | hKK | hAQs | hAJs | hQQ | hJJ | hTT | h66, 0.5)
FACING_4B[3][0] = (hAA | hKK | hAQs | hAJs | hJJ, hAKs | hAKo | hQQ, 0.5)
FACING_4B[3][1] = (hAA | hAKs | hKK | hAQs | hQQ | hJJ, hAJs | hAKo | h66, 0.5)
FACING_4B[3][2] = (hAA | hKK | hAKs | hAKo | hAQs | hAJs | hQQ | hJJ | hTT, h77 | h66, 0.5)
FACING_4B[4][0] = (hAA | hKK | hAKs | hQQ, {}, 0.5)
FACING_4B[4][1] = (hAA | hKK | hAKs | hQQ, hAKo | hJJ, 0.5)
FACING_4B[4][2] = (hAA | hAKs | hKK | hQQ | hJJ, hAKo | hAQs | hTT, 0.5)
FACING_4B[4][3] = (hAA | hAKs | hKK | hQQ | hJJ | hAKo | hTT, hAQs | hAJs | h99, 0.5)
FACING_4B[5][0] = (hAA | hKK | hA6s | hA5s, hAKs | hQQ, 0.5)
FACING_4B[5][1] = (hAA | hKK, hAKs | hQQ, 0.5)
FACING_4B[5][2] = (hAA | hKK | hQQ, hAKs | hAKo | hJJ, 0.5)
FACING_4B[5][3] = (hAA | hKK | hAKs | hQQ | hJJ, hAKo | hAQs | hAJs | hTT, 0.5)
FACING_4B[5][4] = (hAA | hAKo | hKK | hAKs | hAQs | hQQ | hJJ | hTT | h99, hAJs | hATs | hA9s | hA8s | hA7s | hA6s | hA5s | hA3s | hA4s | hKQs | hKJs | hKTs | hQJs | hKQo | hAQo | hAJo | hJTs | h88 | h77 | h66 | h55 | h44 | h33 | h22, 0.5)

FACING_4B[1][2] = (hAA | hKK, hAKs | hQQ, 0.5)
FACING_4B[1][3] = (hAA | hKK, hAKs | hQQ, 0.5)
FACING_4B[1][4] = (hAA | hKK, hAKs | hQQ, 0.5)
FACING_4B[1][5] = (hAA | hKK, hAKs | hQQ, 0.5)
FACING_4B[2][3] = (hAA | hKK, hAKs | hQQ, 0.5)
FACING_4B[2][4] = (hAA | hKK, hAKs | hQQ, 0.5)
FACING_4B[2][5] = (hAA | hKK, hAKs | hQQ, 0.5)
FACING_4B[3][4] = (hAA | hKK, hAKs | hQQ, 0.5)
FACING_4B[3][5] = (hAA | hKK, hAKs | hQQ, 0.5)
FACING_4B[4][5] = (hAA | hKK, hAKs | hQQ, 0.5)

def main():
	from colorama import init
	from termcolor import colored
	init(autoreset=True)
	# todo: determine what to do in missing scenarios
	# todo: determine what to do with large raise
	visualise_range(FACING_RAISE[4][5][0])

	# for hand in hAQo:
		# print(Card.print_pretty_cards(hand))
# main()