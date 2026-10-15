G = int(input())
P = int(input())
docked = 0
maxgates = []
for _ in range(P):
	maxgates.append(int(input()) - 1)

g = [False for _ in range(G)]
docked = 0
for i in range(P):
	maxgate = maxgates[i]
	while g[maxgate] and maxgate >= 0:
		maxgate -= 1
	if maxgate != -1:
		docked += 1
		g[maxgate] = True
	else:
		break
print(docked)
