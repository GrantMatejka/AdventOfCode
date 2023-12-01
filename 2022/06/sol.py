with open('input.txt') as f:
  line = f.readline().strip()
  ch_count = 0
  buffer = []
  for ch in line:
    ch_count += 1
    buffer += ch
    if len(buffer) > 4:
      buffer = buffer[1:]
    if len(buffer) == 4 and len(set(buffer)) == len(buffer):
      print(ch_count)
      break

with open('input.txt') as f:
  line = f.readline().strip()
  ch_count = 0
  buffer = []
  for ch in line:
    ch_count += 1
    buffer += ch
    if len(buffer) > 14:
      buffer = buffer[1:]
    if len(buffer) == 14 and len(set(buffer)) == len(buffer):
      print(ch_count)
      break



