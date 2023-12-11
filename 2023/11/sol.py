import heapq
import math

ex = [
	"...#......",
	".......#..",
	"#.........",
	"..........",
	"......#...",
	".#........",
	".........#",
	"..........",
	".......#..",
	"#...#.....",
]

# DEPRECATED: We don't need to use A* as we can just draw straight lines :facepalm:
def get_shortest_path(grid, src, dest):
	# Pair of point + curr path length
	queue = [(0, 0, src)]
	visited = set()

	width = len(grid)
	height = len(grid[0])

	while len(queue) != 0:
		(dist, cnt, curr_node) = queue.pop(0)
		visited.add(curr_node)

		if dest == curr_node:
			return cnt

		for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
			neighbor = (curr_node[0] + dx, curr_node[1] + dy)
			if neighbor[0] >= 0 and neighbor[0] < width and neighbor[1] >= 0 and neighbor[1] < height and neighbor not in visited:
				heapq.heappush(queue, (math.dist(neighbor, dest), cnt+1, neighbor))
				# queue.append((neighbor, cnt+1))
	print("Cannot find path from:",src,"to:",dest)
	return -1


def get_path_len(src, dest):
	return abs(src[0]-dest[0]) + abs(src[1]-dest[1])

def pt1():
	with open("input.txt") as f:
		lines = f.read().strip().split("\n")
		expanded_universe = []
		for row in lines:
			new_row = ""
			for col_idx, el in enumerate(row):
				if el != '#' and '#' not in [r[col_idx] for r in lines]:
					new_row += "."
				new_row += el
			if "#" not in new_row:
				expanded_universe.append(new_row)
			expanded_universe.append(new_row)

		galaxies = []
		for x, row in enumerate(expanded_universe):
			for y, el in enumerate(row):
				if el == '#':
					galaxies.append((x,y))

		running_sum = 0
		pairs = set()
		for src in galaxies:
			for dest in galaxies:
				if src != dest and (src, dest) not in pairs and (dest, src) not in pairs:
					pairs.add((src, dest))
					path_len = get_path_len(src, dest)
					running_sum += path_len
		print(running_sum)

def pt2():
	with open("input.txt") as f:
		lines = f.read().strip().split("\n")
		expanded_universe = []
		galaxies = []

		# the millionth will always be added separately
		FACTOR = 999_999

		print("Expanding Universe...")
		new_scale_x = 0
		for x, row in enumerate(lines):
			new_row = ""
			new_scale_y = 0
			for y, el in enumerate(row):
				if el != '#' and '#' not in [r[y] for r in lines]:
					new_scale_y += FACTOR
					for _ in range(FACTOR):
						new_row += "."
				elif el == "#":
					galaxies.append((new_scale_x, new_scale_y))
				new_scale_y += 1
				new_row += el
			if "#" not in new_row:
				new_scale_x += FACTOR
				for _ in range(FACTOR):
					expanded_universe.append(new_row)
			new_scale_x += 1
			expanded_universe.append(new_row)


		print("Calculating Path Sums...")
		running_sum = 0
		pairs = set()
		for src in galaxies:
			for dest in galaxies:
				if src != dest and (src, dest) not in pairs and (dest, src) not in pairs:
					pairs.add((src, dest))
					path_len = get_path_len(src, dest)
					running_sum += path_len
		print(running_sum)

pt1()
pt2()
