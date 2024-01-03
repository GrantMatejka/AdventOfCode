import math

ex="""
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""

"""
Part: {x, m, a, s}

Tuple -> (x, m, a, s)
"""

"""
Workflow: key -> (src, operator, num, dest)

Tuple -> (x, m, a, s)
"""

PROP_TO_IDX = {
  'x': 0,
  'm': 1,
  'a': 2,
  's': 3,
}

def getIndexOfEither(s, chars):
  for c in chars:
    if (idx := s.find(c)) != -1:
      return idx

with open("input.txt") as f:
  debug = input("Debug? ")
  src = (ex if int(debug) == 1 else f.read()).strip()
  raw_workflows = src.split("\n\n")[0].split("\n")
  workflows = {}
  for wf_def in raw_workflows:
    [key, raw_conditions] = wf_def.split("{")
    raw_conditions = raw_conditions[:len(raw_conditions)-1]
    conditions = [(PROP_TO_IDX[rc[0]], rc[1], int(rc[getIndexOfEither(rc, ["<", ">"])+1:rc.index(":")]), rc.split(":")[1]) if ":" in rc else tuple([rc]) for rc in raw_conditions.split(",")]
    workflows[key.strip()] = conditions
  parts = [tuple([int(el.split("=")[1]) for el in p[1:len(p)-1].split(",")]) for p in src.split("\n\n")[1].split("\n")]

  count = 0
  for part in parts:
    workflow_key = "in"
    while workflow_key not in ["R", "A"]:
      workflow = workflows[workflow_key]
      for condition in workflow:
        if len(condition) == 1:
          workflow_key = condition[0]
          break

        (src_idx, operator, num, dest) = condition
        src_val = part[src_idx]
        if operator == "<":
          is_valid = src_val < num
        else:
          is_valid = src_val > num
        if is_valid:
          workflow_key = dest
          break
    if workflow_key == "A":
      count += sum(part)

  print(count)

def invert_condition(condition):
  inverted_sign = ">" if "<" == condition[1] else "<"
  adjusted_val = condition[2] - 1 if "<" == condition[1] else condition[2] + 1
  return (condition[0], inverted_sign, adjusted_val)

def build_tree(wf_key):
  if wf_key == "A":
    return [["A"]]
  if wf_key == "R":
    return [["R"]]

  trees = []
  workflow = workflows[wf_key]
  # all previous conditions needs to be false for the next condition to be true
  negated_conditions = set()
  for condition in workflow:
    if len(condition) == 1:
      for t in build_tree(condition[0]):
        trees.append(list(negated_conditions) + t)
      break
    (_s, _o, _n, dest) = condition
    for t in build_tree(dest):
      trees.append(list(negated_conditions) + [condition[:3]] + t)

    negated_conditions.add(invert_condition(condition))
  return trees

def remove_rejected_branches(tree):
  approved_branches = []
  for branch in tree:
    if branch[len(branch)-1] == "A":
      approved_branches.append(branch)
  return approved_branches

def compress_tree(tree):
  ranges = []
  for branch in tree:
    r = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
    # last element in branch will always be "A"
    for step in branch[:len(branch)-1]:
      (key, op, num) = step
      if op == ">" and num > r[key][0]:
        r[key][0] = num
      elif op == "<" and num < r[key][1]:
        r[key][1] = num
    ranges.append(r)
  return ranges


"""
A learning experience day:

Continued off by one errors, but referred to some other solutions for help here
afaict this solution is on the right track?
"""
with open("input.txt") as f:
  debug = input("Debug? ")
  src = (ex if int(debug) == 1 else f.read()).strip()
  raw_workflows = src.split("\n\n")[0].split("\n")
  workflows = {}
  for wf_def in raw_workflows:
    [key, raw_conditions] = wf_def.split("{")
    raw_conditions = raw_conditions[:len(raw_conditions)-1]
    conditions = [(rc[0], rc[1], int(rc[getIndexOfEither(rc, ["<", ">"])+1:rc.index(":")]), rc.split(":")[1]) if ":" in rc else tuple([rc]) for rc in raw_conditions.split(",")]
    workflows[key.strip()] = conditions

  tree = remove_rejected_branches(build_tree("in"))
  for b in tree:
    print(b)
  ranges = compress_tree(tree)

  count = 0
  for r in ranges:
    print(r)
    diff_mul = 1
    for k in r:
      diff_mul *= r[k][1] - r[k][0] + 1
    count += diff_mul

  if debug:
    print("SOL:",167409079868000)
  else:
    print("SOL:",131619440296497)
  print(count)
