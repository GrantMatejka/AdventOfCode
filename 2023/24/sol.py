from z3 import *

ex = """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""

def is_float_in_range(fl, r):
  return r.start <= fl <= r.stop

# ref: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
def find_intersection(l1,l2):
  # Avoid divide by 0
  if ( (l1[0][0]-l1[1][0])*(l2[0][1]-l2[1][1])-(l1[0][1]-l1[1][1])*(l2[0][0]-l2[1][0]) ) == 0:
    return (0, 0)
  px= ( (l1[0][0]*l1[1][1]-l1[0][1]*l1[1][0])*(l2[0][0]-l2[1][0])-(l1[0][0]-l1[1][0])*(l2[0][0]*l2[1][1]-l2[0][1]*l2[1][0]) ) / ( (l1[0][0]-l1[1][0])*(l2[0][1]-l2[1][1])-(l1[0][1]-l1[1][1])*(l2[0][0]-l2[1][0]) )
  py= ( (l1[0][0]*l1[1][1]-l1[0][1]*l1[1][0])*(l2[0][1]-l2[1][1])-(l1[0][1]-l1[1][1])*(l2[0][0]*l2[1][1]-l2[0][1]*l2[1][0]) ) / ( (l1[0][0]-l1[1][0])*(l2[0][1]-l2[1][1])-(l1[0][1]-l1[1][1])*(l2[0][0]-l2[1][0]) )
  return [px, py]

with open("input.txt") as f:
  debug = int(input("Debug? 0 for no, 1 for test case: "))
  src = ex if debug != 0 else f.read()
  lines = [l.split(" @ ") for l in src.strip().split("\n")]
  positions = []
  velocities = []
  for l in lines:
    positions.append(tuple(int(n.strip()) for n in l[0].split(", ")))
    velocities.append(tuple(int(n.strip()) for n in l[1].split(", ")))

  if debug:
    test_zone = range(7, 17)
  else:
    test_zone = range(200000000000000, 400000000000000)

  # Every line is represented by two points
  line_defs = []
  for idx in range(len(positions)):
    (x0, y0, _z0) = positions[idx]
    (vx, vy, _vz) = velocities[idx]

    x1 = vx + x0
    y1 = vy + y0

    p1 = (x0, y0)
    p2 = (x1, y1)

    line_defs.append(((p1, p2), vx, vy))

  intersections = []
  for l1 in line_defs:
    for l2 in line_defs:
      if l1 != l2:
        (l1p, l1vx, l1vy) = l1
        (l2p, l2vx, l2vy) = l2
        intersection_point = find_intersection(l1p, l2p)

        is_forward = True
        # Must follow the velocities "forward"
        dx1 = intersection_point[0] - l1p[0][0]
        # velocities must share sign
        if dx1 / l1vx < 0:
          is_forward = False
        dx2 = intersection_point[0] - l2p[0][0]
        if dx2 / l2vx < 0:
          is_forward = False
        dy1 = intersection_point[1] - l1p[0][1]
        if dy1 / l1vy < 0:
          is_forward = False
        dy2 = intersection_point[1] - l2p[0][1]
        if dy2 / l2vy < 0:
          is_forward = False

        if is_forward:
          intersections.append(intersection_point)
  # We will double count each intersection
  print(sum([1 for intr in intersections if is_float_in_range(intr[0], test_zone) and is_float_in_range(intr[1], test_zone)]) // 2)

with open("input.txt") as f:
  debug = int(input("Debug? 0 for no, 1 for test case: "))
  src = ex if debug != 0 else f.read()
  lines = [l.split(" @ ") for l in src.strip().split("\n")]

  (x, y, z) = (Int('x'), Int('y'), Int('z'))
  (vx, vy, vz) = (Int('vx'), Int('vy'), Int('vz'))

  points = []
  for idx in range(len(positions)):
    (x0, y0, z0) = positions[idx]
    (vx, vy, vz) = velocities[idx]
    points.append((x0, y0, z0, vx, vy, vz))

  T = [Int(f'T{i}') for i in range(len(points))]

  solver = Solver()
  for i in range(len(points)):
    solver.add(x + T[i]*vx - points[i][0] - T[i]*points[i][3] == 0)
    solver.add(y + T[i]*vy - points[i][1] - T[i]*points[i][4] == 0)
    solver.add(z + T[i]*vz - points[i][2] - T[i]*points[i][5] == 0)
  solver.check()
  model = solver.model()
  print(model.eval(x+y+z))
