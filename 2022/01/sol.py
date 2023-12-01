with open("input.txt") as f:
	print("First:", sum(max([[int(i) for i in s.split("\n") if i != ""] for s in f.read().split("\n\n")], key = sum)))

with open("input.txt") as f:
	print("Second:", sum(sorted([l[0] for l in [[sum([int(i) for i in s.split("\n") if i != ""])] for s in f.read().split("\n\n")]])[-3:]))

