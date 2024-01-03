import math

exs = [
  """
  broadcaster -> a, b, c
  %a -> b
  %b -> c
  %c -> inv
  &inv -> a
  """,
  """
  broadcaster -> a
  %a -> inv, con
  &inv -> b
  %b -> con
  &con -> output
  """,
]

with open("input.txt") as f:
  debug = int(input("Debug? 0 for no, 1,2 for test case: ")[0])
  src = exs[debug-1] if debug != 0 else f.read()
  lines = [l.strip().split(" -> ") for l in src.strip().split("\n")]
  graph = {}
  for line in lines:
    raw_key = line[0].strip()

    mod_type = line[0][0]
    edges = [e.strip() for e in line[1].split(",")]
    key = raw_key[1:] if mod_type in ["%", "&"] else raw_key

    graph[key] = { "type": mod_type, "out_edges": edges }
    for e in edges:
      if graph.get(e) == None:
        graph[e] = { "type": None, "out_edges": [] }

  for vertex_key in graph:
    entry = graph[vertex_key]
    if entry['type'] == "%":
      entry['stored_pulse'] = False
    if entry['type'] == "&":
      entry['in_states'] = dict([(e, False) for e in graph if vertex_key in graph[e]['out_edges']])

  count_low = count_high = 0

  for _ in range(1000):
    # message (prev, target, pulse)
    messages = [("button", "broadcaster", False)]
    while len(messages) > 0:
      (prev, target, pulse) = messages.pop()
      node = graph[target]
      if pulse:
        count_high += 1
      else:
        count_low += 1

      if node["type"] == "%":
        # If a flip-flop module receives a high pulse, it is ignored and nothing happens.
        if pulse:
          continue
        # However, if a flip-flop module receives a low pulse, it flips between on and off.
        node["stored_pulse"] = not node["stored_pulse"]
        for out in node["out_edges"]:
          messages.insert(0, (target, out, node["stored_pulse"]))
      # Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected input modules
      elif node["type"] == "&":
        # When a pulse is received, the conjunction module first updates its memory for that input.
        node["in_states"][prev] = pulse
        for out in node["out_edges"]:
          # Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.
          messages.insert(0, (target, out, not all(node["in_states"].values())))
      else:
        for out in node["out_edges"]:
          # Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.
          messages.insert(0, (target, out, pulse))

  print(count_low * count_high)

def pt2():
  with open("input.txt") as f:
    debug = int(input("Debug? 0 for no, 1,2 for test case: ")[0])
    src = exs[debug-1] if debug != 0 else f.read()
    lines = [l.strip().split(" -> ") for l in src.strip().split("\n")]
    graph = {}
    for line in lines:
      raw_key = line[0].strip()

      mod_type = line[0][0]
      edges = [e.strip() for e in line[1].split(",")]
      key = raw_key[1:] if mod_type in ["%", "&"] else raw_key

      graph[key] = { "type": mod_type, "out_edges": edges }
      for e in edges:
        if graph.get(e) == None:
          graph[e] = { "type": None, "out_edges": [] }

    for vertex_key in graph:
      entry = graph[vertex_key]
      if entry['type'] == "%":
        entry['stored_pulse'] = False
      if entry['type'] == "&":
        entry['in_states'] = dict([(e, False) for e in graph if vertex_key in graph[e]['out_edges']])

    parent_high_pulses = {}
    button_press_count = 0
    while True:
      button_press_count += 1
      # message (prev, target, pulse)
      messages = [("button", "broadcaster", False)]
      while len(messages) > 0:
        (prev, target, pulse) = messages.pop()
        node = graph[target]

        end_parent = graph["gf"]
        for in_state_key in end_parent["in_states"]:
          if end_parent["in_states"][in_state_key] == True and parent_high_pulses.get(in_state_key) == None:
            parent_high_pulses[in_state_key] = button_press_count
            if all([parent_high_pulses.get(key) for key in end_parent["in_states"]]):
              print(parent_high_pulses)
              print("LCM:", math.lcm(*[int(n) for n in parent_high_pulses.values()]))
              return

        if node["type"] == "%":
          # If a flip-flop module receives a high pulse, it is ignored and nothing happens.
          if pulse:
            continue
          # However, if a flip-flop module receives a low pulse, it flips between on and off.
          node["stored_pulse"] = not node["stored_pulse"]
          for out in node["out_edges"]:
            messages.insert(0, (target, out, node["stored_pulse"]))
        # Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected input modules
        elif node["type"] == "&":
          # When a pulse is received, the conjunction module first updates its memory for that input.
          node["in_states"][prev] = pulse
          for out in node["out_edges"]:
            # Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.
            messages.insert(0, (target, out, not all(node["in_states"].values())))
        else:
          for out in node["out_edges"]:
            # Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.
            messages.insert(0, (target, out, pulse))
pt2()
