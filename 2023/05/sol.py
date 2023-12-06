import concurrent.futures

ex = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def process_seed_range(idx, seed_ranges, maps):
  print("Searching Seed Range:", seed_ranges[idx], "->", seed_ranges[idx] + seed_ranges[idx + 1])
  locations = {}
  itr = 0
  for seed in range(seed_ranges[idx], seed_ranges[idx] + seed_ranges[idx + 1]):
    itr += 1
    if locations.get(seed) != None:
      continue
    # unmapped src's go to same dest number. e.g. 1 -> 1
    final_location = seed
    for path in ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity"]:
      for mapping in maps[path]:
        if mapping[1] <= final_location < mapping[1] + mapping[2]:
          final_location = mapping[0] + (final_location - mapping[1])
          break
    locations[seed] = final_location
    if itr % 10_000_000 == 0:
      print("Current Min:", min(locations.values()), "From Range:", (seed_ranges[idx], seed_ranges[idx] + seed_ranges[idx + 1]))
  return min(locations.values())

if __name__ == '__main__':
  with open("input.txt") as f:
    inp = f.read()

    lines = inp.strip().split("\n\n")
    seeds = [int(num) for num in lines[0].split(" ")[1:]]
    maps = {}
    for line in lines[1:]:
      # map dict is keyed by first surface in relationship. e.g. seed-to-soil -> seed
      key = line.split(" map:")[0].split("-to-")[0]
      # (dest, src, range)
      maps[key] = [[int(num) for num in m.split(" ")] for m in line.split(" map:")[1].strip().split("\n")]

    paths = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity"]
    locations = []

    for seed in seeds:
      final_location = seed
      for path in paths:
        # unmapped src's go to same dest number. e.g. 1 -> 1
        mappings = maps[path]
        for mapping in mappings:
          if mapping[1] <= final_location < mapping[1] + mapping[2]:
            final_location = mapping[0] + (final_location - mapping[1])
            break
      locations.append(final_location)

    print(min(locations))

  with open("input.txt") as f:
    inp = f.read()

    lines = inp.strip().split("\n\n")

    maps = {}
    for line in lines[1:]:
      # map dict is keyed by first surface in relationship. e.g. seed-to-soil -> seed
      key = line.split(" map:")[0].split("-to-")[0]
      # (dest, src, range)
      maps[key] = [[int(num) for num in m.split(" ")] for m in line.split(" map:")[1].strip().split("\n")]

    seed_ranges = [int(num) for num in lines[0].split(" ")[1:]]
    idx = 0
    itr = 0
    processes = []

    executor = concurrent.futures.ProcessPoolExecutor(max_workers=10)

    while idx < len(seed_ranges):
      processes.append(executor.submit(process_seed_range, idx, seed_ranges, maps))
      idx += 2

    print("Joining processes...")
    print(min([process.result() for process in processes]))
    executor.shutdown()
    print(min(locations.values()))
