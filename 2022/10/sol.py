def is_interesting_cycle(cycle_num):
    return (cycle_num - 20) % 40 == 0 and cycle_num <= 220

# Returns [how much to increment X reg, how many cycles to wait]
def parse_instruction(instr):
    if instr.startswith('addx'):
        return [int(instr.split(" ")[1]), 2]
    else:
        return [0, 1]

with open('input.txt') as f:
    instructions = [l.strip() for l in f.readlines()]
    PC = 0
    X = 1
    cycle = 1
    running_sum = 0

    while PC < len(instructions):
        instr = parse_instruction(instructions[PC])

        for i in range(instr[1]):
            cycle += 1

            if i == instr[1] - 1:
                X += instr[0]

            if (is_interesting_cycle(cycle)):
                running_sum += (cycle * X)
        PC += 1
    print(running_sum)   

 
with open('input.txt') as f:
    CRT = [['.' for i in range(40)] for i in range(6)]
    instructions = [l.strip() for l in f.readlines()]

    PC = 0
    X = 1
    cycle = 1
    running_sum = 0
    pixel_position = 0

    while PC < len(instructions):
        instr = parse_instruction(instructions[PC])

        for i in range(instr[1]):
            cycle += 1

            p_col = pixel_position % 40
            if X - 1 <= p_col <= X + 1:
                CRT[pixel_position // 40][p_col] = "#"
            
            if i == instr[1] - 1:
                X += instr[0]

            pixel_position += 1

        PC += 1

    for row in CRT:
        print(''.join(row))
