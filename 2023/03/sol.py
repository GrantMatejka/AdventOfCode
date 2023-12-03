ex = [
    "467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598..",
]

def is_symbol(ch):
    return not str(ch).isdigit() and ch != '.'

with open("input.txt") as f:
  lines = f.read().split("\n\n")[0].split("\n")
  nums = []
  seen = []

  # find all digits adjacent to a symbol
  for l_x, line in enumerate(lines):
    for l_y, ch in enumerate(line):
      if is_symbol(ch):
        for d_x in (-1, 0, 1):
          for d_y in (-1, 0, 1):
            (n_x, n_y) = (l_x + d_x, l_y + d_y)
            if n_y > 0 and n_y < len(lines[n_x]) and str(lines[n_x][n_y]).isdigit():
              # parse full number
              num_start = n_y 
              num_end = n_y 
              while num_start > 0 and (str(lines[n_x][num_start-1]).isdigit()):
                num_start -= 1
              while num_end < len(lines[n_x]) and (str(lines[n_x][num_end]).isdigit()):
                num_end += 1
              already_added = False
              # we only want to include each part number once
              for i in range(num_start, num_end):
                if (n_x, i) in seen:
                  already_added = True
                else:
                  seen.append((n_x, i))
              
              if not already_added:
                nums.append(int(lines[n_x][num_start:num_end]))
    
  print(sum(nums))

with open("input.txt") as f:
  lines = f.read().split("\n\n")[0].split("\n")
  gears = {}
  seen = []

  # find all digits adjacent to a symbol
  for l_x, line in enumerate(lines):
    for l_y, ch in enumerate(line):
      # we are only interested in gears
      if ch == '*':
        for d_x in (-1, 0, 1):
          for d_y in (-1, 0, 1):
            (n_x, n_y) = (l_x + d_x, l_y + d_y)
            if n_y > 0 and n_y < len(lines[n_x]) and str(lines[n_x][n_y]).isdigit():
              # parse full number
              num_start = n_y 
              num_end = n_y 
              while num_start > 0 and (str(lines[n_x][num_start-1]).isdigit()):
                num_start -= 1
              while num_end < len(lines[n_x]) and (str(lines[n_x][num_end]).isdigit()):
                num_end += 1
              already_added = False
              # we only want to include each part number once
              for i in range(num_start, num_end):
                if (n_x, i) in seen:
                  already_added = True
                else:
                  seen.append((n_x, i))
              
              if not already_added:
                key = (l_x,l_y)
                val = int(lines[n_x][num_start:num_end])
                if key in gears:
                  gears[key].append(val)
                else:
                  gears[key] = [val]
  gear_ratios = []
  for gear in gears.values():
    if len(gear) == 2:
      gear_ratios.append(gear[0] * gear[1])
  print(sum(gear_ratios))