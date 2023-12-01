with open("input.txt") as f:
    lines = [rl.strip() for rl in f.readlines()]
    compartments = [[l[:(len(l) // 2)], l[(len(l) // 2):]]  for l in lines]
    shared_chars = [(set(c[0]) & set(c[1])).pop() for c in compartments]
    points = sum([ord(c) - 96 if c.islower() else ord(c) - 38 for c in shared_chars])
    print(points)

with open("input.txt") as f:
    lines = [rl.strip() for rl in f.readlines()]
    groups = [lines[i:i+3]  for i in range(0, len(lines), 3)]
    shared_chars = [(set(c[0]) & set(c[1]) & set(c[2])).pop() for c in groups]
    points = sum([ord(c) - 96 if c.islower() else ord(c) - 38 for c in shared_chars])
    print(points)