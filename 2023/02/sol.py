ex = [
  "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
  "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
  "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
  "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
  "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

def buildGame(line):
  d = {
    "r": 0,
    "g": 0,
    "b": 0
  }

  if "red" in line:
    d["r"] = int(line.strip().split("red")[0].strip().split(" ")[-1].strip())
  if "green" in line:
    d["g"] = int(line.strip().split("green")[0].strip().split(" ")[-1].strip())
  if "blue" in line:
    d["b"] = int(line.strip().split("blue")[0].strip().split(" ")[-1].strip())
  return d


with open("input.txt") as f:
  lines = f.read().split("\n\n")[0].split("\n")

  # in form (r, g, b)
  conf = {
    "r": 12,
    "g": 13,
    "b": 14
  }

  games = [(int(line.split(":")[0].split(" ")[1]), [buildGame(s) for s in line.split(":")[1].split(";")]) for line in lines]
  possibleGameIds = [g[0] for g in games if all([s['r'] <= conf['r'] and s['g'] <= conf['g'] and s['b'] <= conf['b'] for s in g[1]])]

  print(sum(possibleGameIds))

with open("input.txt") as f:
  lines = f.read().split("\n\n")[0].split("\n")
  
  games = [(int(line.split(":")[0].split(" ")[1]), [buildGame(s) for s in line.split(":")[1].split(";")]) for line in lines]
  gameMinimums = [{"r": max(g[1], key=lambda p: p["r"])["r"], "g": max(g[1], key=lambda p: p["g"])["g"],"b": max(g[1], key=lambda p: p["b"])["b"]} for g in games]
  powers = [gm["r"]*gm["g"]*gm["b"] for gm in gameMinimums]

  print(sum(powers))