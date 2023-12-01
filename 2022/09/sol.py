import math

def get_direction_modifier(direction):
    if direction == 'R':
        return [1, 0]
    elif direction == 'L':
        return [-1, 0]
    elif direction == 'U':
        return [0, 1]
    elif direction == 'D':
        return [0, -1]

def are_touching(head, tail):
    deltas = [abs(head[0] - tail[0]), abs(head[1] - tail[1])]
    return deltas[0] <= 1 and deltas[1] <= 1

def sign(num):
    return -1 if num < 0 else 0 if num == 0 else 1

def get_adjustment(head, tail):
    deltas = [
        head[0] - tail[0],
        head[1] - tail[1]
    ]

    return [
        sign(deltas[0]),
        sign(deltas[1]),
    ]

with open('input.txt') as f:
    motions = [[m[0], int(m[1])] for m in [l.strip().split(" ") for l in f.readlines()]]
    head = [0, 0]
    tail = [0, 0]
    tail_locations = set()

    for motion in motions:
        d_modifier = get_direction_modifier(motion[0])
        for _ in range(motion[1]):
            head = [
                head[0] + d_modifier[0],
                head[1] + d_modifier[1]
            ]

            if not are_touching(head, tail):
                adjustment = get_adjustment(head, tail)
                tail = [
                    tail[0] + adjustment[0],
                    tail[1] + adjustment[1]
                ]
                tail_locations.add(str(tail))
            
    print(len(tail_locations))

with open('input.txt') as f:
    motions = [[m[0], int(m[1])] for m in [l.strip().split(" ") for l in f.readlines()]]
    knots = [
        [0, 0], # Head
        [0, 0], # 1
        [0, 0], # 2
        [0, 0], # 3
        [0, 0], # 4
        [0, 0], # 5
        [0, 0], # 6
        [0, 0], # 7
        [0, 0], # 8
        [0, 0], # 9
    ]
    tail_locations = set()
    tail_locations.add(str([0,0]))

    for motion in motions:
        d_modifier = get_direction_modifier(motion[0])
        for _ in range(motion[1]):
            knots[0] = [
                knots[0][0] + d_modifier[0],
                knots[0][1] + d_modifier[1]
            ]

            for knot_idx in range(1, len(knots)):
                head = knots[knot_idx - 1]
                tail = knots[knot_idx]
                if not are_touching(head, tail):
                    adjustment = get_adjustment(head, tail)
                    knots[knot_idx] = [
                        tail[0] + adjustment[0],
                        tail[1] + adjustment[1]
                    ]

            tail_locations.add(str(knots[len(knots) - 1]))
            
    print(len(tail_locations))