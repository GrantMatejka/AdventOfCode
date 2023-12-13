
ex = [
	[
		"#.##..##.",
		"..#.##.#.",
		"##......#",
		"##......#",
		"..#.##.#.",
		"..##..##.",
		"#.#.##.#.",
	],
	[
		"#...##..#",
		"#....#..#",
		"..##..###",
		"#####.##.",
		"#####.##.",
		"..##..###",
		"#....#..#",
	],
]

ex2 = [
	[
		"..##..##...",
		"..#.##.#.##",
		"...#.#.#...",
		"##.#.####..",
		"...###.#.##",
		"######.#.##",
		"######..#.#",
	]
]

def pt1():
	with open("input.txt") as f:
		lines = [l.split("\n") for l in f.read().strip().split("\n\n")]

		n = 0
		for terrain in lines:
			x = 0
			y = 0
			while x < len(terrain):
				lower = x
				upper = x + 1
				mirrored = False
				while lower >= 0 and upper < len(terrain):
					if terrain[lower] != terrain[upper]:
						mirrored = False
						break
					else:
						mirrored = True
					lower -= 1
					upper += 1

				if mirrored:
					# aoc is 1 indexed
					n += (x + 1) * 100
				x += 1

			while y < len(terrain[0]):
				lower = y
				upper = y + 1
				mirrored = False
				while lower >= 0 and upper < len(terrain[0]):
					if "".join([t[lower] for t in terrain]) != "".join([t[upper] for t in terrain]):
						mirrored = False
						break
					else:
						mirrored = True
					lower -= 1
					upper += 1

				if mirrored:
					# aoc is 1 indexed
					n += (y + 1)
				y += 1
		print(n)

def get_refl_row(terrain):
	x = 0
	while x < len(terrain):
		lower = x
		upper = x + 1
		mirrored = False
		while lower >= 0 and upper < len(terrain):
			if terrain[lower] != terrain[upper]:
				mirrored = False
				break
			else:
				mirrored = True
			lower -= 1
			upper += 1

		if mirrored:
			return x
		x += 1
	return -1

def get_refl_col(terrain):
	y = 0
	while y < len(terrain[0]):
		lower = y
		upper = y + 1
		mirrored = False
		while lower >= 0 and upper < len(terrain[0]):
			if "".join([t[lower] for t in terrain]) != "".join([t[upper] for t in terrain]):
				mirrored = False
				break
			else:
				mirrored = True
			lower -= 1
			upper += 1

		if mirrored:
			return y
		y += 1
	return -1

def get_all_refl_rows(terrain):
	x = 0
	res = []
	while x < len(terrain):
		lower = x
		upper = x + 1
		mirrored = False
		while lower >= 0 and upper < len(terrain):
			if terrain[lower] != terrain[upper]:
				mirrored = False
				break
			else:
				mirrored = True
			lower -= 1
			upper += 1

		if mirrored:
			res.append(x)
		x += 1
	return res

def get_all_refl_cols(terrain):
	y = 0
	res = []
	while y < len(terrain[0]):
		lower = y
		upper = y + 1
		mirrored = False
		while lower >= 0 and upper < len(terrain[0]):
			if "".join([t[lower] for t in terrain]) != "".join([t[upper] for t in terrain]):
				mirrored = False
				break
			else:
				mirrored = True
			lower -= 1
			upper += 1

		if mirrored:
			res.append(y)
		y += 1
	return res

def calc_terrain(terrain):
	orig_col = get_refl_col(terrain)
	orig_row = get_refl_row(terrain)

	for x in range(len(terrain)):
		for y in range(len(terrain[0])):
			new_terrain = [l for l in terrain]
			if new_terrain[x][y] == ".":
				new_terrain[x] = new_terrain[x][:y] + "#" + new_terrain[x][y+1:]
			else:
				new_terrain[x] = new_terrain[x][:y] + "." + new_terrain[x][y+1:]

			new_cols = get_all_refl_cols(new_terrain)
			new_rows = get_all_refl_rows(new_terrain)
			# We know there will be EXACTLY one other reflection
			if len(new_cols) == 2 or len(new_cols) > 0 and orig_col not in new_cols:
				return [n for n in new_cols if n != orig_col][0] + 1
			if len(new_rows) == 2 or len(new_rows) > 0 and orig_row not in new_rows:
				return ([n for n in new_rows if n != orig_row][0] + 1) * 100

	raise ValueError("Never found smudge for:", terrain)


def pt2():
	with open("input.txt") as f:
		lines = [l.split("\n") for l in f.read().strip().split("\n\n")]

		n = 0
		for terrain in lines:
			n += calc_terrain(terrain)
		print(n)

pt1()
pt2()
