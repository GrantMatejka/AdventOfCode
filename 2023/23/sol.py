exs = [
  """
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
  """,
]

with open("input.txt") as f:
  debug = int(input("Debug? 0 for no, 1 for test case: "))
  src = exs[debug-1] if debug != 0 else f.read()
  m = src.strip().split("\n")

  completed = []
  queue = [((0, 1), set())]
  while len(queue) > 0:
    (pos, visited) = queue.pop()
    visited.add(pos)

    # Exit will always be to left of bottom right corner
    if pos == (len(m)-1, len(m[0])-2):
      completed.append(len(visited)-1)
      continue

    char = m[pos[0]][pos[1]]
    neighbors = [(-1,0), (1,0), (0,-1), (0,1)]
    if char == "v":
      neighbors = [(1, 0)]
    elif char == ">":
      neighbors = [(0 ,1)]
    for (dx ,dy) in neighbors:
      new_pos = (pos[0] + dx, pos[1] + dy)
      if 0 <= new_pos[0] < len(m) and 0 <= new_pos[1] < len(m[0]) and m[new_pos[0]][new_pos[1]] != "#" and new_pos not in visited:
        queue.append((new_pos, visited.copy()))
  completed.sort()
  print(completed)
  print(max(completed))

"""
Patience is a virtue
"""
with open("input.txt") as f:
  debug = int(input("Debug? 0 for no, 1 for test case: "))
  src = exs[debug-1] if debug != 0 else f.read()
  m = src.strip().split("\n")

  start = (0, 1)
  finish = (len(m)-1, len(m[0])-2)

  completed = set()
  queue = [(start, set(), 0)]
  while queue:
    (pos, visited, visited_count) = queue.pop()

    # Exit will always be to left of bottom right corner
    if pos == finish:
      completed.add(visited_count)
      # through trial/error I know it's bigger than this
      if visited_count > 6400:
        print(max(completed))
      continue

    visited.add(pos)
    visited_count += 1

    for (dx ,dy) in [(-1,0), (1,0), (0,-1), (0,1)]:
      (x, y) = (pos[0] + dx, pos[1] + dy)
      if 0 <= x < len(m) and 0 <= y < len(m[0]) and m[x][y] != "#" and (x, y) not in visited:
        queue.append(((x, y), visited.copy(), visited_count))
  print(max(completed))

