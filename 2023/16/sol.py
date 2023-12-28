ex = """
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
"""

DIRS = {
  "N": (-1, 0),
  "S": (1, 0),
  "E": (0, 1),
  "W": (0, -1)
}

DIR_CHANGES = {
  ".": {
    "N": ["N"],
    "S": ["S"],
    "E": ["E"],
    "W": ["W"]
  },
  "\\": {
    "N": ["W"],
    "S": ["E"],
    "E": ["S"],
    "W": ["N"]
  },
  "/": {
    "N": ["E"],
    "S": ["W"],
    "E": ["N"],
    "W": ["S"]
  },
  "|": {
    "N": ["N"],
    "S": ["S"],
    "E": ["N", "S"],
    "W": ["N", "S"]
  },
  "-": {
    "N": ["E", "W"],
    "S": ["E", "W"],
    "E": ["E"],
    "W": ["W"]
  },
}

global_visited = set()

def trace_path(lines, node, incoming_dir):
  node_and_dir_visited = set()
  node_visited = set()

  # Dir = N, S, E, W
  nodes = [(node, incoming_dir)]
  while len(nodes) > 0:
    (node, incoming_dir) = nodes.pop()
    node_and_dir_visited.add((node, incoming_dir))
    node_visited.add(node)
    sym = lines[node[0]][node[1]]
    next_dirs = DIR_CHANGES[sym][incoming_dir]

    for d in next_dirs:
      (dx, dy) = DIRS[d]
      new_node = (node[0] + dx, node[1] + dy)
      new_node_and_dir = (new_node, d)
      if new_node[0] >= 0 and new_node[0] < len(lines) and new_node[1] >= 0 and new_node[1] < len(lines[0]) and new_node_and_dir not in node_and_dir_visited:
        nodes.append(((new_node[0], new_node[1]), d))

  return len(node_visited)

def pt1():
  with open("input.txt") as f:
    debug = input("Debug: ")
    src = ex if int(debug) == 1 else f.read()
    lines = src.strip().split("\n")
    print(trace_path(lines, (0,0), "E"))

def pt2():
  with open("input.txt") as f:
    debug = input("Debug: ")
    src = ex if int(debug) == 1 else f.read()
    lines = src.strip().split("\n")

    confs = []
    for y in range(len(lines)):
      confs.append(((y, 0), "E"))
      confs.append(((y, len(lines[0])-1), "W"))
    
    for x in range(len(lines[0])):
      confs.append(((0, x), "S"))
      confs.append(((len(lines)-1,x), "N"))

    print(max([trace_path(lines, node, dir) for (node, dir) in confs]))

pt1()
pt2()
