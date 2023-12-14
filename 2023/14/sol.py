ex = [
	"O....#....",
	"O.OO#....#",
	".....##...",
	"OO.#O....O",
	".O.....O#.",
	"O.#..O.#.#",
	"..O..#O..O",
	".......O..",
	"#....###..",
	"#OO..#....",
]

def pt1():
	with open("input.txt") as f:
		lines = f.read().strip().split("\n")
		for x in range(len(lines)):
			for y in range(len(lines[0])):
				if lines[x][y] == "O":
					roll_idx = x - 1
					col = [line[y] for line in lines]
					rolled = False
					while roll_idx >= 0 and col[roll_idx] == ".":
						rolled = True
						roll_idx -= 1
					if rolled:
						# make up for one too many iterations
						roll_idx += 1
						lines[x] = lines[x][:y] + "." + lines[x][y+1:]
						lines[roll_idx] = lines[roll_idx][:y] + "O" + lines[roll_idx][y+1:]
		load = 0
		for i in range(len(lines)):
			load += (len(lines) - i) * sum([1 for el in lines[i] if el == "O"])
		print("Pt1 North Load:",load)

def roll_north(lines):
	for x in range(len(lines)):
		for y in range(len(lines[0])):
			if lines[x][y] == "O":
				roll_idx = x - 1
				col = [line[y] for line in lines]
				rolled = False
				while roll_idx >= 0 and col[roll_idx] == ".":
					rolled = True
					roll_idx -= 1
				if rolled:
					# make up for one too many iterations
					roll_idx += 1
					lines[x] = lines[x][:y] + "." + lines[x][y+1:]
					lines[roll_idx] = lines[roll_idx][:y] + "O" + lines[roll_idx][y+1:]
	return lines

def roll_east(lines):
	for x in range(len(lines)):
		for y in range(len(lines[0])-1,-1,-1):
			if lines[x][y] == "O":
				roll_idx = y + 1
				row = lines[x]
				rolled = False
				while roll_idx < len(row) and row[roll_idx] == ".":
					rolled = True
					roll_idx += 1
				if rolled:
					# make up for one too many iterations
					roll_idx -= 1
					lines[x] = lines[x][:y] + "." + lines[x][y+1:]
					lines[x] = lines[x][:roll_idx] + "O" + lines[x][roll_idx+1:]
	return lines

def roll_south(lines):
	for x in range(len(lines[0])-1, -1, -1):
		for y in range(len(lines[0])):
			if lines[x][y] == "O":
				roll_idx = x + 1
				col = [line[y] for line in lines]
				rolled = False
				while roll_idx < len(col) and col[roll_idx] == ".":
					rolled = True
					roll_idx += 1
				if rolled:
					# make up for one too many iterations
					roll_idx -= 1
					lines[x] = lines[x][:y] + "." + lines[x][y+1:]
					lines[roll_idx] = lines[roll_idx][:y] + "O" + lines[roll_idx][y+1:]
	return lines

def roll_west(lines):
	for x in range(len(lines)):
		for y in range(len(lines[0])):
			if lines[x][y] == "O":
				roll_idx = y - 1
				row = lines[x]
				rolled = False
				while roll_idx >= 0 and row[roll_idx] == ".":
					rolled = True
					roll_idx -= 1
				if rolled:
					# make up for one too many iterations
					roll_idx += 1
					lines[x] = lines[x][:y] + "." + lines[x][y+1:]
					lines[x] = lines[x][:roll_idx] + "O" + lines[x][roll_idx+1:]
	return lines

def calc_load(lines):
	load = 0
	for i in range(len(lines)):
		load += (len(lines) - i) * sum([1 for el in lines[i] if el == "O"])
	return load

def pt2():
	with open("input.txt") as f:
		lines = f.read().strip().split("\n")

		seen = {}
		loads = []
		for idx in range(1_000_000_000):
			lines = roll_east(roll_south(roll_west(roll_north(lines))))

			key = "".join([str(l) for l in lines])
			# we have a loop, identify where we're at
			if loop_start := seen.get(key):
				loop_len = idx - loop_start
				phase = (1_000_000_000 - loop_start) % loop_len
				print("Pt2 North Load:",loads[loop_start + phase - 1])
				break
			else:
				seen[key] = idx
				loads.append(calc_load(lines))
pt1()
pt2()
