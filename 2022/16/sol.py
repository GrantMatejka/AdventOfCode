import re


class Valve:
    def __init__(self, data):
        self.name = data[0]
        self.flow = int(data[1])
        self.connections = data[2].split(", ")

    def pretty_print(self):
        print("Valve", self.name, " Flow:", self.flow)
        print("Connections:", self.connections, "\n")

    def __hash__(self):
        return hash(self.name)


REGEX = r"Valve (\w+) has flow rate=(\d+); tunnel(?:s*) lead(?:s*) to valve(?:s*) (.*)"
T = 30


def score_traversal(valves, open_valves):
    score = 0
    for ov in open_valves:
        valve = valves[ov[0]]
        score += (T - ov[1]) * valve.flow
    return score


def traverse(valves, visited, current_valve_name, open_valve, open_valves, minute):
    if minute == T:
        return score_traversal(valves, open_valves)

    m = minute + 1
    cv = valves[current_valve_name]

    traversals = []
    if open_valve:
        # append the valve we are opening and WHEN we opened it
        open_valves.add((current_valve_name, minute))
        # continue traversal with updated open valves
        traversals.append(
            traverse(valves, visited, current_valve_name, False, open_valves, m)
        )
    elif current_valve_name not in [ov[0] for ov in open_valves]:
        # if we haven't open this valve yet, go ahead and try to open it
        traversals.append(traverse(valves, visited, cv.name, True, open_valves, m))

    # Move to each neighbor
    for n in cv.connections:
        traversals.append(traverse(valves, visited, n, False, open_valves, m))

    return max(traversals)


with open("test_input.txt") as f:
    valves = [Valve(re.match(REGEX, line).groups()) for line in f.readlines()]
    valve_dict = {}
    for v in valves:
        valve_dict[v.name] = v

    chunk = {
        "traversal": "",
        "name": "",
        "should_open": "",
        "minute": "",
    }

    print(traverse(valve_dict, [], "AA", False, set(), 0))

