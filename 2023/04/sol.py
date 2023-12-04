with open("input.txt") as f:
  lines = f.read().split("\n\n")[0].split("\n")
  games = [([int(num) for num in line.split(":")[1].split("|")[0].split(" ") if num.isnumeric()], [int(num) for num in line.split(":")[1].split("|")[1].split(" ") if num.isnumeric()]) for line in lines]
  sol = []
  for game in games:
    score = 0
    for winning_num in game[0]:
        if winning_num in game[1]:
            if score == 0:
                score = 1
            else:
                score *= 2
    sol.append(score)
  print(sum(sol))

with open("input.txt") as f:
  lines = f.read().split("\n\n")[0].split("\n")
  cards = {}
  totals = {}
  for line in lines:
    card_id = int(line.split(":")[0].split(" ")[len(line.split(":")[0].split(" "))-1].strip())
    cards[card_id] = (card_id, [int(num) for num in line.split(":")[1].split("|")[0].split(" ") if num.isnumeric()], [int(num) for num in line.split(":")[1].split("|")[1].split(" ") if num.isnumeric()])
    totals[card_id] = 0
  scratchers = [v for v in cards.values()]
  while len(scratchers) > 0:
    scratcher = scratchers.pop()
    scratcher_id = scratcher[0]
    totals[scratcher_id] = totals[scratcher_id] + 1

    winning_numbers_count = sum([1 for num in scratcher[1] if num in scratcher[2]])

    while winning_numbers_count > 0:
        scratchers.append(cards[scratcher_id + winning_numbers_count])
        winning_numbers_count -= 1

  print(sum(totals.values()))
