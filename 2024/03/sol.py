import re

ex = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

with open("input.txt") as f:
    # src = ex.strip().split("\n")
    src = f.read().split("\n\n")[0].split("\n")

    total = 0
    for line in src:
        matches = re.findall("mul\(\d+,\d+\)", line)
        pairs = [(int(n.split(",")[0][4:]),int(n.split(",")[1][:-1])) for n in matches]
        for pair in pairs:
            total += (pair[0] * pair[1])
    print(total)


with open("input.txt") as f:
    # src = ex.strip().split("\n")
    src = f.read().split("\n\n")[0].split("\n")

    total = 0
    enabled = True
    for line in src:
        instructions = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
        for inst in instructions:
            if "don't" in inst:
                enabled = False
            elif "do" in inst:
                enabled = True
            elif enabled:
                pair = (int(inst.split(",")[0][4:]),int(inst.split(",")[1][:-1]))
                total += (pair[0] * pair[1])
    print(total)