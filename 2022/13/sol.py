import ast
from functools import cmp_to_key

def isEqual(left, right):
  # If exactly one value is an integer, convert the integer to a list which contains that integer as its only value
  R = [right] if not isinstance(right, list) else right
  L = [left] if not isinstance(left, list) else left

  idx = 0
  while True:
    # If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
    if idx == len(L) and len(L) == len(R):
      return 0

    # If the left list runs out of items first, the inputs are in the right order.
    if idx == len(L):
      return -1
    # If the right list runs out of items first, the inputs are not in the right order.
    elif idx == len(R):
      return 1

    lVal = L[idx]
    rVal = R[idx]

    if isinstance(lVal, int) and isinstance(rVal, int):
      # If the left integer is lower than the right integer, the inputs are in the right order.
      if lVal < rVal:
        return -1
      # If the left integer is higher than the right integer, the inputs are not in the right order.
      elif lVal > rVal:
        return 1
    else:
      result = isEqual(lVal, rVal)
      if result != 0:
        return result

    idx += 1


with open('input.txt', 'r') as f:
  parse = [p.split('\n') for p in f.read().split('\n\n')]
  pairs = [[ast.literal_eval(pair[0]), ast.literal_eval(pair[1])] for pair in parse]

  result = [isEqual(pair[0], pair[1]) for pair in pairs]
  print(sum([i + 1 if result[i] == -1 else 0 for i in range(len(result))]))
  
  dividers = [[[2]], [[6]]]
  packets = [*dividers]
  for pair in pairs:
    packets.append(pair[0])
    packets.append(pair[1])
  packets.sort(key=cmp_to_key(isEqual))

  product = 1
  for i, packet in enumerate(packets):
    if packet in dividers:
      product *= i + 1
  print(product)
