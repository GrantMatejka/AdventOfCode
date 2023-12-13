from functools import cache

ex = [
	"???.### 1,1,3",
	".??..??...?##. 1,1,3",
	"?#?#?#?#?#?#?#? 1,3,1,6",
	"????.#...#... 4,1,1",
	"????.######..#####. 1,6,5",
	"?###???????? 3,2,1",
]

def is_row_valid(row, conf):
	lens = [len(grp) for grp in "".join(row).split(".") if len(grp) > 0]
	if len(lens) != len(conf):
		return False
	for idx in range(len(lens)):
		if lens[idx] != conf[idx]:
			return False
	return True

def pt1():
	with open("input.txt") as f:
		lines = f.read().strip().split("\n")
		rows = [(line.split(" ")[0], [int(n) for n in line.split(" ")[1].split(",")]) for line in lines]
		combinations = []
		for (row, rule) in rows:
			possibilities = [row]
			while len(possibilities) > 0:
				pos = possibilities.pop()
				pos_idx = -1
				try:
					pos_idx = pos.index("?")
				except ValueError:
					pass
				if pos_idx != -1:
					possibilities.append(pos[:pos_idx] + "." + pos[pos_idx+1:])
					possibilities.append(pos[:pos_idx] + "#" + pos[pos_idx+1:])
				else:
					combinations.append((pos, rule))
		print(sum([1 for combo in combinations if is_row_valid(combo[0], combo[1])]))

"""
Borrowed from: https://topaz.github.io/paste/#XQAAAQDXBAAAAAAAAAAzHIoib6poHLpewxtGE3pTrRdzrponKxDhfDpmqTf7ST2L/3+FXWVlhsIM1KNMkEHo676M7mB+glfKzWzNybchN72ocVdubWfYfFubVB6Az44A3RUnm14KK5zaRyktpuwAhL0BGfYJvm1BYn7XI53V0xgZN9CpJUXlOEq9usK7J3HBz/bOVz1rKbSrIKyl55XbA16mUJ2mm38VdDMctDM1FXKvlUSESn9WjdNY7HLi9ovDsIPqbvt5ZVs8SkMLZF0twppwtlsW6O1Pmg9tNJkc62EFOFvCLNI8/zUK4MdhJbbAEbdktnn/zCVtUiFDrSTQ6MztnJVXfnrEkDLiFp4OeSTh4FArSfTlE1Pj+haWNgkwu6RMG/vqLj4EIn9LSMjBBRj4YedlUfjHsKSBrb1LPJGR4Jj4zUMswOVx2wlTK7+Tm8BL5w+4s8VbhmsO0v7CFHm5E5lJHJZ5kO+SifipCQuu2JTMXx8hi6pQtQN5ARI1EHTYhSll/aeSqRGKmVeo9yFiDaE/3TVUcKK70PLZ8QD0+8iswXXaKw6iM6pgCQYL3oZH+a73yc5+pIsZc8d1G/bbGEasbZdwHZ8VorE6u21kEoLXyqoKKFKZD77vsg4yIo4nQ6ctMTCxiAi4hZBE/LS86INuAKmV1/5RsmPfaeiMqjy460/e9RU3hRNX+cGpIMMwSm7lF8jEhV3ean087r9U+8jNe3laV38Uukp3pez0uHlkfb7K8gffGpQyZrr9hKhOnM7c1hBvaRZJSMptUipEhbs/wfw83jhGPqJg9N7pBCOI0JlOd5lpgUSDGBSkObsLY7IZEybHPlDV/96dhrw=
"""
@cache
def process_row(row, groups):
	row = row.lstrip(".")

	# If we're empty
	if len(row) == 0:
		return int(len(groups) == 0)

	if len(groups) == 0:
		return 0 if "#" in row else 1

	if row[0] == "#":
		# No room
		if len(row) < groups[0]:
			return 0
		# Can't create consistent group
		if "." in row[:groups[0]]:
			return 0
		elif len(row) == groups[0]:
			# Perfect size final group
			return int(len(groups) == 1)
		elif row[groups[0]] == "#":
			# too close to next group
			return 0
		else:
			return process_row(row[groups[0]+1:], groups[1:])
	return process_row('#'+row[1:],groups) + process_row(row[1:],groups)

def pt2():
	with open("input.txt") as f:
		lines = f.read().strip().split("\n")
		rows = []
		for line in lines:
			row = "?".join([line.split(" ")[0]]*5)
			rule = tuple([int(n) for n in line.split(" ")[1].split(",")]*5)
			rows.append((row, rule))

		cnt = 0
		for (row, rule) in rows:
			cnt += process_row(row, rule)
		print(cnt)

pt1()
pt2()
