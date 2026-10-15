from itertools import permutations

X = int(input())
same = dict()
for _ in range(X):
	pair = input().split()
	if pair[0] not in same:
		same[pair[0]] = [pair[1]]
	else:
		same[pair[0]].append(pair[1])
	# if pair[1] not in same:
	# 	same[pair[1]] = [pair[0]]
	# else:
	# 	same[pair[1]].append(pair[0])
Y = int(input())
diff = {tuple(input().split()) for _ in range(Y)}
G = int(input())
groups = [input().split() for _ in range(G)]

violations = 0

for group in groups:
	for p in permutations(group, 2):
		if p in diff:
			violations += 1
			# print(p)
	for m in group:
		if m in same:
			for mp in same[m]:
				if mp not in group:
					# print(m, same[m])
					violations += 1

print(violations)
