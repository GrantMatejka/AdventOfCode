import heapq

ex = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

ex2 = """
111111111111
999999999991
999999999991
999999999991
999999999991
"""

DIRS = {
	"N": (-1, 0),
	"S": (1, 0),
	"E": (0, 1),
	"W": (0, -1)
}

OPP_DIRS = {
	"N": "S",
	"S": "N",
	"E": "W",
	"W": "E"
}


def pt1():
	with open("input.txt") as f:
		debug = input("Debug? 0/1 -> ")
		lines = (ex if int(debug) == 1 else f.read()).strip().split("\n")

		height = len(lines)
		width = len(lines[0])

		# (point, direction, seq_count)
		visited = set()
		# (point, direction, seq_count, running_total)
		nodes = [(0, 0, 0, False, 0)]
		end_totals = []
		while len(nodes) > 0:
			(running_total, x, y, direction, seq_count) = heapq.heappop(nodes)
			point = (x, y)

			# Hmm, it was exceptionally faster to include this check when processing a node, not adding one
			if (point, direction, seq_count) in visited:
				continue

			visited.add((point, direction, seq_count))

			if point[0] == height - 1 and point[1] == width - 1:
				end_totals.append(running_total)

			for new_direction in DIRS:
				if new_direction == OPP_DIRS.get(direction):
					continue
				(dx, dy) = DIRS[new_direction]
				new_point = (point[0] + dx, point[1] + dy)
				new_seq_count = seq_count + 1 if new_direction == direction else 1
				inbounds = new_point[0] >= 0 and new_point[0] < height and new_point[1] >= 0 and new_point[1] < width
				if inbounds and new_seq_count < 4:
					heapq.heappush(nodes, (running_total + int(lines[new_point[0]][new_point[1]]), new_point[0], new_point[1], new_direction, new_seq_count))
		print(min(end_totals))

def pt2():
	with open("input.txt") as f:
		debug = input("Debug? 0/1 -> ")
		lines = (ex2 if int(debug) == 1 else f.read()).strip().split("\n")

		height = len(lines)
		width = len(lines[0])

		# (point, direction, seq_count)
		visited = set()
		# (point, direction, seq_count, running_total)
		nodes = [(0, 0, 0, False, 0)]
		end_totals = []
		while len(nodes) > 0:
			(running_total, x, y, direction, seq_count) = heapq.heappop(nodes)
			point = (x, y)

			# Hmm, it was exceptionally faster to include this check when processing a node, not adding one
			if (point, direction, seq_count) in visited:
				continue

			visited.add((point, direction, seq_count))

			# Need to move 4 blocks before we are allowed to stop
			if point[0] == height - 1 and point[1] == width - 1 and seq_count >= 4:
				end_totals.append(running_total)

			for new_direction in DIRS:
				if new_direction == OPP_DIRS.get(direction):
					continue
				(dx, dy) = DIRS[new_direction]
				new_point = (point[0] + dx, point[1] + dy)
				inbounds = new_point[0] >= 0 and new_point[0] < height and new_point[1] >= 0 and new_point[1] < width
				new_seq_count = seq_count + 1 if new_direction == direction else 1
				is_allowed = (new_seq_count <= 10 if direction == False or new_direction == direction else seq_count >= 4)
				if inbounds and is_allowed:
					heapq.heappush(nodes, (running_total + int(lines[new_point[0]][new_point[1]]), new_point[0], new_point[1], new_direction, new_seq_count))
		print(min(end_totals))

pt1()
pt2()





