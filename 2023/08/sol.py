import math

ex =[
	"RL",
	"",
	"AAA = (BBB, CCC)",
	"BBB = (DDD, EEE)",
	"CCC = (ZZZ, GGG)",
	"DDD = (DDD, DDD)",
	"EEE = (EEE, EEE)",
	"GGG = (GGG, GGG)",
	"ZZZ = (ZZZ, ZZZ)",
]

ex2 = [
	"LLR",
	"",
	"AAA = (BBB, BBB)",
	"BBB = (AAA, ZZZ)",
	"ZZZ = (ZZZ, ZZZ)",
]

with open("input.txt") as f:
	src = f.read().strip().split("\n")

	instrs = src[0]
	m = {}
	for line in src[2:]:
		src = line.split(" = ")[0]
		l = line.split(" = ")[1].split(", ")[0][1:]
		r = line.split(" = ")[1].split(", ")[1][:-1]
		m[src] = {
			"L": l,
			"R": r
		}

	count = 0
	loc = "AAA"
	while loc != "ZZZ":
		loc = m[loc][instrs[count % len(instrs)]]
		count += 1
	print(count)

ex3 = [
	"LR",
	"",
	"11A = (11B, XXX)",
	"11B = (XXX, 11Z)",
	"11Z = (11B, XXX)",
	"22A = (22B, XXX)",
	"22B = (22C, 22C)",
	"22C = (22Z, 22Z)",
	"22Z = (22B, 22B)",
	"XXX = (XXX, XXX)",
]

def pt2_brute_force():
	with open("input.txt") as f:
		src = f.read().strip().split("\n")

		instrs = src[0]
		m = {}
		for line in src[2:]:
			src = line.split(" = ")[0]
			l = line.split(" = ")[1].split(", ")[0][1:]
			r = line.split(" = ")[1].split(", ")[1][:-1]
			m[src] = {
				"L": l,
				"R": r
			}

		count = 0
		cycle_counts = {}
		roots = [loc for loc in m.keys() if loc.endswith('A')]
		for root in roots:
			cycle_counts[root] = False
		locs = roots
		while len([loc for loc in locs if not loc.endswith('Z')]) != 0:
			if (count % 1_000_000 == 0):
				print(count,locs)

			locs = [m[loc][instrs[count % len(instrs)]] for loc in locs]
			count += 1

		print(count)

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

with open("input.txt") as f:
	src = f.read().strip().split("\n")

	instrs = src[0]
	m = {}
	for line in src[2:]:
		src = line.split(" = ")[0]
		l = line.split(" = ")[1].split(", ")[0][1:]
		r = line.split(" = ")[1].split(", ")[1][:-1]
		m[src] = {
			"L": l,
			"R": r
		}

	count = 0
	cycle_counts = {}
	roots = [loc for loc in m.keys() if loc.endswith('A')]
	for root in roots:
		cycle_counts[root] = False
	locs = roots
	while not all(cycle_counts.values()):
		for idx in range(len(locs)):
			if locs[idx].endswith('Z') and cycle_counts.get(roots[idx]) == False:
					cycle_counts[roots[idx]] = count

		locs = [m[loc][instrs[count % len(instrs)]] for loc in locs]
		count += 1

	vals = [n for n in cycle_counts.values()]
	x = vals[0]
	for v in vals[1:]:
		x = lcm(x, v)

	print(x)
