ex = [
	"Time:      7  15   30",
	"Distance:  9  40  200"
]

with open("input.txt") as f:
	src = f.read().strip().split("\n")
	lines = [line.split()[1:] for line in src]
	# (time, record distance)
	races = []
	for idx in range(len(lines[0])):
		races.append((int(lines[0][idx]), int(lines[1][idx])))

	total_wins = []
	for race in races:
		wins = 0
		for hold_time in range(race[0] + 1):
			speed = hold_time
			remaining_time = race[0] - hold_time
			total = speed * remaining_time
			if total > race[1]:
				wins += 1
		total_wins.append(wins)

	total = total_wins[0]
	for win in total_wins[1:]:
		total *= win
	print(total)

with open("input.txt") as f:
	src = f.read().strip().split("\n")
	lines = ["".join(line.split()[1:]) for line in src]
	# (time, record distance)
	race = (int(lines[0]), int(lines[1]))

	wins = 0
	for hold_time in range(race[0] + 1):
		if hold_time * (race[0] - hold_time) > race[1]:
			wins += 1

	print(wins)
