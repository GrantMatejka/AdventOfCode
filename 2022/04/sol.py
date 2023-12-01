
with open("input.txt") as f:
    lines = [rl.strip() for rl in f.readlines()]
    ranges = [[int(n) for n in r] for r in[r.replace("-", ",").split(",") for r in lines]]
    overlaps = [1 if (r[0] >= r[2] and r[1] <= r[3]) or (r[2] >= r[0] and r[3] <= r[1]) else 0 for r in ranges]
    score = sum(overlaps)
    print(score)
    
with open("input.txt") as f:
    lines = [rl.strip() for rl in f.readlines()]
    ranges = [[int(n) for n in r] for r in[r.replace("-", ",").split(",") for r in lines]]
    overlaps = [1 if (r[2] <= r[1] <= r[3] or r[2] <= r[0] <= r[3]) or (r[0] <= r[2] <= r[1] or r[0] <= r[3] <= r[1]) else 0 for r in ranges]
    score = sum(overlaps)
    print(score)