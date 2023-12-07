from functools import cmp_to_key

ex = [
	"32T3K 765",
	"T55J5 684",
	"KK677 28",
	"KTJJT 220",
	"QQQJA 483",
]

cards = "23456789TJQKA"

def process_hand(hand):
	d = {}
	for card in hand:
		if d.get(card) != None:
			d[card] = d[card] + 1
		else:
			d[card] = 1
	return d

def first_ordering(hand_d):
	if 5 in hand_d.values():
		return 7
	if 4 in hand_d.values():
		return 6
	if 3 in hand_d.values() and 2 in hand_d.values():
		return 5
	if 3 in hand_d.values():
		return 4
	# two pair
	if len([1 for v in hand_d.values() if v == 2]) == 2:
		return 3
	if 2 in hand_d.values():
		return 2
	else:
		return 1

# 1 means h1 > h2, -1 means h1 < h2
def second_ordering(h1, h2):
	idx = 0
	while idx < len(h1):
		if cards.index(h1[idx]) > cards.index(h2[idx]):
			return 1
		if cards.index(h1[idx]) < cards.index(h2[idx]):
			return -1
		idx += 1

def comparator(hb1, hb2):
	h1 = hb1[0]
	h2 = hb2[0]
	h1_r = first_ordering(process_hand((h1)))
	h2_r = first_ordering(process_hand((h2)))
	if h1_r > h2_r:
		return 1
	elif h1_r < h2_r:
		return -1
	else:
		s_ord = second_ordering(h1, h2)
		if s_ord == 1:
			return 1
		elif s_ord == -1:
			return -1
	return 0

with open("input.txt") as f:
	src = f.read().strip().split("\n")
	hands = [(l.split(" ")[0], int(l.split(" ")[1])) for l in src]

	ranked_hands = sorted(hands,key=cmp_to_key(comparator))
	score = 0
	for idx, hb in enumerate(ranked_hands):
		score += (idx + 1) * hb[1]
	print(score)

cards_pt2 = "J23456789TQKA"

def process_hand_pt2(hand):
	d = {}
	for card in hand:
		if d.get(card) != None:
			d[card] = d[card] + 1
		else:
			d[card] = 1
	return d

def first_ordering_pt2(hand_d):
	jokers = hand_d.pop("J", 0)

	sorted_pairs = [n for n in reversed(sorted(hand_d.values()))]
	max_pairs = jokers
	if max_pairs != 5:
		max_pairs = sorted_pairs[0] + jokers

	if max_pairs == 5:
		return 7
	if max_pairs == 4:
		return 6
	if max_pairs == 3 and sorted_pairs[1] == 2:
		return 5
	if max_pairs == 3:
		return 4
	# two pair
	if max_pairs == 2 and sorted_pairs[1] == 2:
		return 3
	if max_pairs == 2:
		return 2
	else:
		return 1

def second_ordering_pt2(h1, h2):
	idx = 0
	while idx < len(h1):
		if cards_pt2.index(h1[idx]) > cards_pt2.index(h2[idx]):
			return 1
		if cards_pt2.index(h1[idx]) < cards_pt2.index(h2[idx]):
			return -1
		idx += 1

def comparator_pt2(hb1, hb2):
	h1 = hb1[0]
	h2 = hb2[0]
	h1_r = first_ordering_pt2(process_hand((h1)))
	h2_r = first_ordering_pt2(process_hand((h2)))

	if h1_r > h2_r:
		return 1
	elif h1_r < h2_r:
		return -1
	else:
		s_ord = second_ordering_pt2(h1, h2)
		if s_ord == 1:
			return 1
		elif s_ord == -1:
			return -1
	return 0

with open("input.txt") as f:
	src = f.read().strip().split("\n")
	hands = [(l.split(" ")[0], int(l.split(" ")[1])) for l in src]

	ranked_hands = sorted(hands,key=cmp_to_key(comparator_pt2))
	score = 0
	for idx, hb in enumerate(ranked_hands):
		score += (idx + 1) * hb[1]
	print(score,[x for x in reversed(ranked_hands)])
