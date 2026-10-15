slimy = {(0, 0)}
slimed = 0
snailpos = [0, 0]
T = int(input())

for _ in range(T):
	movement = input()
	if movement[0] == "N":
		for __ in range(int(movement[1:])):
			snailpos[1] -= 1
			if tuple(snailpos) in slimy:
				slimed += 1
			slimy.add(tuple(snailpos))
	if movement[0] == "E":
		for __ in range(int(movement[1:])):
			snailpos[0] += 1
			if tuple(snailpos) in slimy:
				slimed += 1
			slimy.add(tuple(snailpos))
	if movement[0] == "S":
		for __ in range(int(movement[1:])):
			snailpos[1] += 1
			if tuple(snailpos) in slimy:
				slimed += 1
			slimy.add(tuple(snailpos))
	if movement[0] == "W":
		for __ in range(int(movement[1:])):
			snailpos[0] -= 1
			if tuple(snailpos) in slimy:
				slimed += 1
			slimy.add(tuple(snailpos))

print(slimed)
