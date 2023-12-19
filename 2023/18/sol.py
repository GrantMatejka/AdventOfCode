import numpy as np
from matplotlib.path import Path

ex = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

DIRS = {
	"U": (-1, 0),
	"D": (1, 0),
	"L": (0, -1),
	"R": (0, 1),
}

def pt1():
	with open("input.txt") as f:
		debug = input("Debug? 0/1 -> ")
		lines = (ex if int(debug) == 1 else f.read()).strip().split("\n")
		cmds = [(line.split(" ")[0], int(line.split(" ")[1])) for line in lines]

		print("Digging... ", "Plan len:", len(cmds), ",", end="")
		path_points = []
		loc = (0, 0)
		for cmd in cmds:
			(direction, num) = cmd
			while num > 0:
				path_points.append(loc)
				(dx, dy) = DIRS[direction]
				loc = (loc[0] + dx, loc[1] + dy)
				num -= 1
		print(len(path_points), "path points")

		min_height = min([v[0] for v in path_points])
		max_height = max([v[0] for v in path_points])
		min_width = min([v[1] for v in path_points])
		max_width = max([v[1] for v in path_points])

		print("Calculating Area")
		path = Path(path_points)
		count = 0
		for x in range(min_height, max_height + 1):
			for y in range(min_width, max_width + 1):
				if (x,y) in path_points or path.contains_point((x, y)):
					count += 1
		print(count)


# x, y are parallel arrays of (x,y) pairs
def shoelace_area(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

def pt2():
	with open("input.txt") as f:
		debug = input("Debug? 0/1 -> ")
		lines = (ex if int(debug) == 1 else f.read()).strip().split("\n")
		DIGIT_TO_DIR = {"0": "R", "1": "D", "2": "L", "3": "U"}
		cmds = [(DIGIT_TO_DIR[line.split(" ")[2][7]], int(line.split(" ")[2][2:7], 16)) for line in lines]

		print("Digging...")
		perimeter_len = 0
		loc = (0, 0)
		xs = []
		ys = []
		for cmd in cmds:
			(direction, num) = cmd
			perimeter_len += num
			(dx, dy) = DIRS[direction]
			loc = (loc[0] + (num * dx), loc[1] + (num * dy))
			xs.append(loc[0])
			ys.append(loc[1])

		# Shoelace, this will be the wrong area, so we need to correct with pick's
		area = shoelace_area(xs, ys)
		# Pick's theorem
		enclosed = int(area + 1 - (perimeter_len // 2))
		print("Perimeter:", perimeter_len, "Area:", area, "Enclosed:", enclosed)
		print("Total:", perimeter_len + enclosed)

pt1()
pt2()
