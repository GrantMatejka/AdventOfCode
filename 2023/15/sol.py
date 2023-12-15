ex = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

def hash_str(s):
	num = 0
	for ch in s:
		char_code = ord(ch)
		num += char_code
		num *= 17
		num = num % 256
	return num

def pt1():
	with open("input.txt") as f:
		lines = f.read().strip().split(",")
		print(sum([hash_str(l) for l in lines]))

def pt2():
	with open("input.txt") as f:
		debug = input("Debug? 0/1 -> ")
		lines = (ex if debug == 1 else f.read().strip()).split(",")
		boxes = dict([(i, []) for i in range(0,255)])
		cmds = [tuple(l.split("=")) if "=" in l else tuple([l.split("-")[0]]) for l in lines ]
		for cmd in cmds:
			label = cmd[0]
			box_key = hash_str(label)

			if len(cmd) == 1:
				new_boxes = []
				for entry in boxes[box_key]:
					if entry[0] != label:
						new_boxes.append(entry)
				boxes[box_key] = new_boxes
				pass
			else:
				replaced = False
				for idx, entry in enumerate(boxes[box_key]):
					if entry[0] == label:
						replaced = True
						boxes[box_key][idx] = cmd
						break
				if not replaced:
					boxes[box_key].append(cmd)

		score = 0
		for box_key in boxes:
			for idx, entry in enumerate(boxes[box_key]):
				score += (box_key + 1) * (idx + 1) * int(entry[1])
		print(score)

pt1()
pt2()
