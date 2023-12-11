from matplotlib.path import Path

examples = [
    [
        ".....",
        ".S-7.",
        ".|.|.",
        ".L-J.",
        ".....",
    ],
    [
        "..F7.",
        ".FJ|.",
        "SJ.L7",
        "|F--J",
        "LJ...",
    ],
    [
        "...........",
        ".S-------7.",
        ".|F-----7|.",
        ".||.....||.",
        ".||.....||.",
        ".|L-7.F-J|.",
        ".|..|.|..|.",
        ".L--J.L--J.",
        "...........",
    ],
    [
        ".F----7F7F7F7F-7....",
        ".|F--7||||||||FJ....",
        ".||.FJ||||||||L7....",
        "FJL7L7LJLJ||LJ.L-7..",
        "L--J.L7...LJS7F-7L7.",
        "....F-J..F7FJ|L7L7L7",
        "....L7.F7||L7|.L7L7|",
        ".....|FJLJ|FJ|F7|.LJ",
        "....FJL-7.||.||||...",
        "....L---J.LJ.LJLJ...",
    ],
    [
        "FF7FSF7F7F7F7F7F---7",
        "L|LJ||||||||||||F--J",
        "FL-7LJLJ||||||LJL-77",
        "F--JF--7||LJLJ7F7FJ-",
        "L---JF-JLJ.||-FJLJJ7",
        "|F|F-JF---7F7-L7L|7|",
        "|FFJF7L7F-JF7|JL---7",
        "7-L-JL7||F7|L7F-7F7|",
        "L.L7LFJ|||||FJL7||LJ",
        "L7JLJL-JLJLJL--JLJ.L",
    ],
]

NAVIGATABLE_NEIGHBORS = {
    "N": ['|', '7', 'F'],
    "S": ['|', 'L', 'J'],
    "E": ['-', '7', 'J'],
    "W": ['-', 'L', 'F'],
}

DIR = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
}

VALID_DIRS = {
    'S': ['N', 'S', 'E', 'W'],
    '|': ["N", "S"],
    '-': ["W", "E"],
    'L': ["E", "N"],
    'J': ["W", "N"],
    '7': ["W", "S"],
    'F': ["E", "S"],
    '.': []
}


def get_dir(lines, loc):
  sym = get_sym(lines, loc)
  return VALID_DIRS[sym]


def get_sym(lines, loc):
  return lines[loc[0]][loc[1]]


def can_move_to_neighbor(dir, neighbor_symbol):
  return neighbor_symbol in NAVIGATABLE_NEIGHBORS[dir]


def find_loop_len(lines, start_loc):
  ctr = 0
  loc = start_loc
  visited = set()

  while loc not in visited:
    visited.add(loc)
    ctr += 1

    for dir in get_dir(lines, loc):
      (dx, dy) = DIR[dir]
      new_loc = (loc[0] + dx, loc[1] + dy)
      if can_move_to_neighbor(dir, get_sym(
          lines, new_loc)) and new_loc not in visited:
        loc = new_loc
        break

  return ctr


with open('input.txt') as f:
  debug = int(
      input(f"Debug?\n0 for no, or [1..{len(examples)}] for test case: "))
  lines = examples[debug - 1] if debug else f.read().strip().split('\n')

  starting_loc = False
  for x in range(len(lines)):
    for y in range(len(lines[x])):
      if lines[x][y] == 'S':
        starting_loc = (x, y)
        break
    if starting_loc is not False:
      break

  loop_len = find_loop_len(lines, starting_loc)
  print("Full Loop:", loop_len, "Furthest Point:", loop_len // 2)


def find_loop(lines, start_loc):
  ctr = 0
  loc = start_loc
  visited = []

  while loc not in visited:
    visited.append(loc)
    ctr += 1

    for dir in get_dir(lines, loc):
      (dx, dy) = DIR[dir]
      new_loc = (loc[0] + dx, loc[1] + dy)
      if can_move_to_neighbor(dir, get_sym(
          lines, new_loc)) and new_loc not in visited:
        loc = new_loc
        break

  return visited


with open('input.txt') as f:
  debug = int(
      input(f"Debug?\n0 for no, or [1..{len(examples)}] for test case: "))
  lines = examples[debug - 1] if debug else f.read().strip().split('\n')

  starting_loc = False
  for x in range(len(lines)):
    for y in range(len(lines[x])):
      if lines[x][y] == 'S':
        starting_loc = (x, y)
        break
    if starting_loc is not False:
      break

  loop_points = find_loop(lines, starting_loc)
  enclosed = 0
  path = Path(loop_points)
  for x in range(len(lines)):
    for y in range(len(lines[x])):
      point = (x, y)
      if point in loop_points:
        continue
      if path.contains_point(point):
        enclosed += 1
  print("Enclosed Points:", enclosed)
