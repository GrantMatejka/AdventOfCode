def parse(blobs):
    monkeys = []
    for blob in blobs:
        lines = blob.split("\n")
        items = [int(i.strip()) for i in lines[1].split(':')[1].split(",")]
        operation = lines[2].split('=')[1].strip().split(" ")
        divisible = int(lines[3].split(' ')[5])
        true = int(lines[4].split(' ')[9])
        false = int(lines[5].split(' ')[9])
        monkeys.append({
            'items': items,
            'operation': operation,
            'divisible': divisible,
            'true': true,
            'false': false
        })
    return monkeys

def apply_operation(worry, op):
    parse = [worry if o == 'old' else int(o) if o.isdigit() else o for o in op]
    operator = op[1]

    if operator == '*':
        return parse[0] * parse[2]
    elif operator == '+':
        return parse[0] + parse[2]
    else:
        raise Exception(f'Unknown Operator: {operator}')

with open('input.txt') as f:
    monkeys = parse(f.read().split("\n\n"))
    
    round = 0
    inspections = [0 for _ in monkeys]
    while round < 20:
        for idx, m in enumerate(monkeys):
            items = m['items']
            while len(m['items']) > 0:
                inspections[idx] += 1
                item = m['items'][0]
                m['items'] = m['items'][1:]
                worry = apply_operation(item, m['operation'])
                bored = worry // 3
                if bored % m['divisible'] == 0:
                    monkeys[m['true']]['items'].append(bored)
                else:
                    monkeys[m['false']]['items'].append(bored)
        round += 1
    first = max(inspections)
    inspections.remove(first)
    second = max(inspections)

    print(first * second)

# Had to google a hint on this one...
with open('input.txt') as f:
    monkeys = parse(f.read().split("\n\n"))
    
    round = 1
    inspections = [0 for _ in monkeys]
    modulo = 1
    for m in monkeys:
        modulo *= m['divisible']

    while round <= 10_000:
        for idx, m in enumerate(monkeys):
            items = m['items']
            while len(m['items']) > 0:
                inspections[idx] += 1
                item = m['items'][0]
                m['items'] = m['items'][1:]
                worry = apply_operation(item, m['operation'])
                bored = worry % modulo
                if bored % m['divisible'] == 0:
                    monkeys[m['true']]['items'].append(bored)
                else:
                    monkeys[m['false']]['items'].append(bored)
        round += 1
    first = max(inspections)
    inspections.remove(first)
    second = max(inspections)

    print(first * second)