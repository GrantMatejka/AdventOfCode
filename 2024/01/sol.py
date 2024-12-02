with open("input.txt") as f:
    l1 = []
    l2 = []
    for loc_pair in f.read().split("\n\n")[0].split("\n"):
        loc_pair = loc_pair.split()
        l1.append(int(loc_pair[0]))
        l2.append(int(loc_pair[1]))

    l1 = sorted(l1)
    l2 = sorted(l2)

    total = 0
    for i in range(len(l1)):
        total += abs(l1[i] - l2[i])
    print(total)

with open("input.txt") as f:
    l1 = []
    l2 = []
    for loc_pair in f.read().split("\n\n")[0].split("\n"):
        loc_pair = loc_pair.split()
        l1.append(int(loc_pair[0]))
        l2.append(int(loc_pair[1]))

    total = 0
    for i in range(len(l1)):
        occ = l2.count(l1[i])
        total += (l1[i] * occ)
    print(total)