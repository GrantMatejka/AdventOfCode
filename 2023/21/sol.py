
import numpy as np

exs = [
  """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
  """,
]

with open("input.txt") as f:
  debug = int(input("Debug? 0 for no, 1 for test case: ")[0])
  src = exs[debug-1] if debug != 0 else f.read()
  garden = [l.strip() for l in src.strip().split("\n")]

  height = range(len(garden))
  width = range(len(garden[0]))

  start_loc = (0, 0)
  for x in height:
    for y in width:
      if garden[x][y] == "S":
        start_loc = (x, y)

  ITERATIONS = 6 if debug else 64

  queue = set([start_loc])
  for _ in range(ITERATIONS):
    next_queue = set()
    while len(queue) > 0:
      loc = queue.pop()
      for neighbor in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_loc = (loc[0] + neighbor[0], loc[1] + neighbor[1])
        if new_loc[0] in height and new_loc[1] in width and garden[new_loc[0]][new_loc[1]] != "#" and new_loc not in next_queue:
          next_queue.add(new_loc)
    queue = next_queue

  print(len(queue))

# Raw BFS too slow for pt 2
def get_plots_for_n(garden, n):
  height = len(garden)
  width = len(garden[0])

  start_loc = (0, 0)
  for x in range(height):
    for y in range(width):
      if garden[x][y] == "S":
        start_loc = (x, y)


  queue = set([start_loc])
  for _ in range(n):
    next_queue = set()
    while queue:
      loc = queue.pop()
      for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_loc = (loc[0] + dx, loc[1] + dy)
        if garden[new_loc[0] % height][new_loc[1] % width] != "#":
          next_queue.add(new_loc)
    queue = next_queue

  return len(queue)

with open("input.txt") as f:
  debug = int(input("Debug? 0 for no, 1 for test case: ")[0])
  src = exs[debug-1] if debug != 0 else f.read()
  garden = [l.strip() for l in src.strip().split("\n")]

  # step count = (height * N) + 65
  height = len(garden)
  STEP_COUNT = 26501365
  N = (STEP_COUNT - 65) // height

  """
  As a learning experience: Referred to some online materials for this one
  """

  print("Calculating Initial Points")
  a1 = get_plots_for_n(garden, 65)
  a2 = get_plots_for_n(garden, 65 + height)
  a3 = get_plots_for_n(garden, 65 + (height * 2))

  print("Solve Exponential")
  v = np.matrix([[0, 0, 1], [1, 1, 1], [4, 2, 1]])
  b = np.array([a1, a2, a3])
  x = np.linalg.solve(v, b)

  # PLOTS = A*N^2 + B*N + C
  print("part 2:", int(x[0] * N**2 + x[1] * N + x[2]))
