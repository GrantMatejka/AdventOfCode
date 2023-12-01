import re

REGEX = r"Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)"


def m_distance(p_1, p_2):
    return int(abs(p_1[0] - p_2[0]) + abs(p_1[1] - p_2[1]))


def width(p, d, y):
    return ((2 * d) + 1) - (abs(m_distance(p, [p[0], y])) * 2)


with open("input.txt") as f:
    Y = 2000000
    groups = [re.match(REGEX, line).groups() for line in f.readlines()]
    points = [
        [(int(group[0]), int(group[1])), (int(group[2]), int(group[3]))]
        for group in groups
    ]
    beacons = set([(int(group[2]), int(group[3])) for group in groups])
    distances = [[point[0], m_distance(point[0], point[1])] for point in points]
    pois = [
        point
        for point in distances
        if point[0][1] <= Y <= point[0][1] + point[1]
        or point[0][1] >= Y >= point[0][1] - point[1]
    ]
    center_widths = [([p[0][0], Y], width(p[0], p[1], Y)) for p in pois]
    coverage = set()
    for cw in center_widths:
        side_width = (cw[1] - 1) // 2
        for s in range(cw[0][0] - side_width - 1, cw[0][0] + side_width):
            point = (s, Y)
            if point not in beacons:
                coverage.add(s)

    print(len(coverage))


with open("input.txt") as f:
    BOUND = 4000000
    groups = [re.match(REGEX, line).groups() for line in f.readlines()]
    points = [
        [(int(group[0]), int(group[1])), (int(group[2]), int(group[3]))]
        for group in groups
    ]
    beacons = set([(int(group[2]), int(group[3])) for group in groups])
    sensors = [[point[0], m_distance(point[0], point[1])] for point in points]

    for [s, d] in sensors:
        for dx in range(-d - 1, d + 1):
            for my in [1, -1]:
                dy = my * ((d + 1) - dx)
                p = (s[0] + dx, s[1] + dy)

                if not (0 <= p[0] <= BOUND and 0 <= p[1] <= BOUND):
                    continue

                unreachable = True
                for other_sensor, other_distance in sensors:
                    if m_distance(other_sensor, p) <= other_distance:
                        unreachable = False
                        break

                if unreachable:
                    sol = 4000000 * p[0] + p[1]
                    print(sol)
                    exit()
