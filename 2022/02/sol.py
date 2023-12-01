with open("input.txt") as f:
    print(sum([round[1] + (6 if round[0] - round[1] in [-1, 2] else 3 if round[0] == round[1] else 0) for round in [[1 + ord(round.strip().split(" ")[0]) - ord('A'), 1 + ord(round.strip().split(" ")[1]) - ord('X')] for round in f.readlines()]]))

with open("input.txt") as f:
    print(sum([round[1] * 3 + ([[3, 1, 2], [1, 2, 3], [2, 3, 1]])[round[0]][round[1]] for round in [[ord(round.strip().split(" ")[0]) - ord('A'), ord(round.strip().split(" ")[1]) - ord('X')] for round in f.readlines()]]))
