with open("input.txt") as f:
  lines = f.read().split("\n\n")[0].split("\n")
  sol = []
  for line in lines:
    firstNum = False
    secondNum = False
    for i in range(len(line) + 1):
      if (i < len(line) and not firstNum and line[i].isdigit()):
        firstNum = int(line[i])
      if (i != 0 and not secondNum and line[-i].isdigit()):
        secondNum = int(line[-i])
      if (firstNum and secondNum):
        sol.append(firstNum * 10 + secondNum)
        break
  print(sum(sol))

with open("input.txt") as f:
  digits = { "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9 }

  lines = [l for l in f.read().split("\n\n")[0].split("\n") if l != ""]
  sol = []
  for line in lines:
    indeces = []
    for key in digits.keys():
      try:
        # If we go by both directions we will get min/max pos of each digit
        indeces.append((key, line.index(key)))
        indeces.append((key, line.rindex(key)))
      except ValueError:
        False

    minDigit = min(indeces, key = lambda x: x[1])
    maxDigit = max(indeces, key = lambda x: x[1])

    sol.append(digits[minDigit[0]] * 10 + digits[maxDigit[0]])

  print(sum(sol))

