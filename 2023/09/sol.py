ex = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45",
]
with open('input.txt') as f:
  src = f.read().strip().split("\n")
  lines = [[int(n) for n in l.split(" ")] for l in src]

  extrapolations = []
  for line in lines:
    idx = 1
    extrapolation_tree = [line]
    new_curr_line = []
    curr_line = line
    while any([n != 0 for n in curr_line]):
      new_curr_line.append(curr_line[idx] - curr_line[idx - 1])
      idx += 1
      if idx == len(curr_line):
        idx = 1
        curr_line = new_curr_line
        extrapolation_tree.append(new_curr_line)
        new_curr_line = []
    extrapolation = 0
    for level in reversed(extrapolation_tree):
      extrapolation += level[len(level) - 1]
    extrapolations.append(extrapolation)
  print(sum(extrapolations))

with open('input.txt') as f:
  src = f.read().strip().split("\n")
  lines = [[int(n) for n in l.split(" ")] for l in src]

  extrapolations = []
  for line in lines:
    idx = len(line) - 1
    extrapolation_tree = [line]
    new_curr_line = []
    curr_line = line
    while any([n != 0 for n in curr_line]):
      new_curr_line = [curr_line[idx] - curr_line[idx - 1]] + new_curr_line
      idx -= 1
      if idx == 0:
        idx = len(new_curr_line) - 1
        curr_line = new_curr_line
        extrapolation_tree.append(new_curr_line)
        new_curr_line = []
    extrapolation = 0
    for level in reversed(extrapolation_tree):
      extrapolation = level[0] - extrapolation
    extrapolations.append(extrapolation)
  print(sum(extrapolations))
