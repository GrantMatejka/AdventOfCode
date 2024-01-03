import copy

exs = [
  """
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
  """,
]

with open("input.txt") as f:
  debug = int(input("Debug? 0 for no, 1 for test case: ")[0])
  src = exs[debug-1] if debug != 0 else f.read()
  bricks = [[[int(n) for n in p.split(",")] for p in l.strip().split("~")] for l in src.strip().split("\n")]

  # A dictionary of each brick at each level
  z_dict = {}
  print("Mapping Bricks to Level")
  for brick in bricks:
    # Add one to upper bound to make it inclusive
    new_brick = (range(brick[0][0], brick[1][0]+1), range(brick[0][1], brick[1][1]+1))
    # Duplicate any brick that covers multiple Z's
    z_coverage = brick[1][2] - brick[0][2]
    while z_coverage >= 0:
      z = brick[0][2] + z_coverage
      if entry := z_dict.get(z):
        entry.append(new_brick)
      else:
        z_dict[z] = [new_brick]
      z_coverage -= 1

  print("Dropping Bricks")
  for level in sorted([n for n in z_dict.keys()]):
    if level == 1:
      continue
    # For every brick at this level
    for brick in z_dict[level]:
      brick_level = level
      while True:
        level_beneath = brick_level - 1
        if level_beneath == 0:
          break
        elif not z_dict.get(level_beneath):
          z_dict[level_beneath] = []

        # If we have no x or y intersections, we can fall
        can_fall = all(set(brick[0]).intersection(brick_beneath[0]) == set() or set(brick[1]).intersection(brick_beneath[1]) == set() for brick_beneath in z_dict[level_beneath])
        if not can_fall:
          break

        try:
          z_dict[brick_level] = z_dict[brick_level].remove(brick) or []
        except ValueError:
          z_dict[brick_level] = []
        z_dict[level_beneath].append(brick)
        brick_level = level_beneath

  print("Calculating Supports")
  count_eliminate = 0
  already_accounted_for = set()
  for level in sorted([n for n in z_dict.keys()]):
      level_above = level + 1
      bricks = z_dict[level]
      for brick in bricks:
        cannot_be_removed = False
        new_supporting_bricks = bricks.copy()
        new_supporting_bricks.remove(brick) or []

        for supporting_brick in new_supporting_bricks:
          cannot_be_removed = any(len(set(supporting_brick[0]).intersection(brick_beneath[0])) == 0 and len(set(supporting_brick[1]).intersection(brick_beneath[1])) == 0 for brick_beneath in new_supporting_bricks)
          if cannot_be_removed and supporting_brick not in already_accounted_for:
            already_accounted_for.add(supporting_brick)
            break
        if not cannot_be_removed:
          count_eliminate += 1

  print(count_eliminate)


"""
Another learning day :( needed help from online as seen below
"""
infile = open("input.txt")

cubes = {}

for i, line in enumerate(infile):
    p0, p1 = (tuple(map(int, p.split(","))) for p in line.strip().split("~"))
    cubes[i] = (p0, p1)

gminx = min(min(x0, x1) for ((x0, _, _), (x1, _, _)) in cubes.values())
gminy = min(min(y0, y1) for ((_, y0, _), (_, y1, _)) in cubes.values())
gmaxx = max(max(x0, x1) for ((x0, _, _), (x1, _, _)) in cubes.values())
gmaxy = max(max(y0, y1) for ((_, y0, _), (_, y1, _)) in cubes.values())

grid = dict(((x,y,0), -1) for x in range(gminx, gmaxx+1) for y in range(gminy, gmaxy+1))

# lower cubes starting from the lowest ones, stopping when they collide with something
to_lower = list(range(len(cubes)))
to_lower.sort(key = lambda i: min(cubes[i][0][2], cubes[i][1][2]))
resting_on = {}
while to_lower:

    c_i = to_lower.pop(0)
    c = cubes[c_i]

    rest = set()
    rest_z = -1

    cminx = min(c[0][0], c[1][0])
    cminy = min(c[0][1], c[1][1])
    cminz = min(c[0][2], c[1][2])
    cmaxx = max(c[0][0], c[1][0])
    cmaxy = max(c[0][1], c[1][1])
    cmaxz = max(c[0][2], c[1][2])

    for ((gx, gy, gz), gi) in grid.items():
        if gx >= cminx and gx <= cmaxx and gy >= cminy and gy <= cmaxy:
            if gz > rest_z:
                rest_z = gz
                rest = set([gi])
            elif gz == rest_z:
                rest.add(gi)

    resting_on[c_i] = rest

    new_z = rest_z + 1
    delta_z = new_z - cminz
    c = ((c[0][0], c[0][1], c[0][2] + delta_z),
         (c[1][0], c[1][1], c[1][2] + delta_z))
    cminz = min(c[0][2], c[1][2])
    cmaxz = max(c[0][2], c[1][2])

    for z in range(cminz, cmaxz+1):
        for y in range(cminy, cmaxy+1):
            for x in range(cminx, cmaxx+1):
                assert((x, y, z) not in grid)
                grid[(x, y, z)] = c_i

total = 0
can_disintegrate = set(range(len(cubes)))
for ri, rs in resting_on.items():
    if len(rs) == 1:
        r, = rs
        can_disintegrate.discard(r)
print(len(can_disintegrate))

for c_i in range(len(cubes)):
    if c_i in can_disintegrate:
        continue
    fall = set()
    new_fall = set([c_i])
    while len(new_fall) > len(fall):
        fall.update(new_fall)
        for c_j in range(len(cubes)):
            if all(ro in new_fall for ro in resting_on[c_j]):
                new_fall.add(c_j)
    total += len(fall) - 1

print(total)
