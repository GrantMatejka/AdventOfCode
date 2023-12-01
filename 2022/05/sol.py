import re

def parseFile(f):
  stacks = [[] for _ in range(9)]
  moves = []
  for line in f.readlines():
    if '[' in line:
      for i in range(0, len(line), 4):
        if line[i+1].isalpha():
          stacks[int(i/4)] += line[i+1]
    elif line.startswith('move'):
      result = re.search('move (\d+) from (\d+) to (\d+)', line)
      if len(result.groups()) == 3:
        groups = result.groups()
        moves += [[int(groups[0]), int(groups[1]) - 1, int(groups[2]) - 1]]

  return [stacks, moves]

with open('input.txt') as f:
  [stacks, moves] = parseFile(f)

  for move in moves:
    count = move[0]
    src = move[1]
    sink = move[2]

    crates = stacks[src][:count]
    crates.reverse()
    stacks[src] = stacks[src][count:]
    stacks[sink] = crates + stacks[sink]

  result = ''.join([stack[0] for stack in stacks if len(stack) > 0])

  print(result)

with open('input.txt') as f:
  [stacks, moves] = parseFile(f)

  for move in moves:
    count = move[0]
    src = move[1]
    sink = move[2]

    crates = stacks[src][:count]
    stacks[src] = stacks[src][count:]
    stacks[sink] = crates + stacks[sink]

  result = ''.join([stack[0] for stack in stacks if len(stack) > 0])

  print(result)
