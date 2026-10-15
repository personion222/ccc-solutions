import sys
sys.setrecursionlimit(100000)

M = int(input())
N = int(input())

room = [[int(x) for x in input().split()] for _ in range(M)]
visited = [[False for _ in range(N)] for __ in range(M)]

coords = {}
for ridx, row in enumerate(room):
	for cidx, num in enumerate(row):
		if num in coords:
			coords[num].append((ridx + 1, cidx + 1))
		else:
			coords[num] = [(ridx + 1, cidx + 1)]

def room_bfs(pos):
	global visited
	if pos == (1, 1):
		return True
	if visited[pos[0] - 1][pos[1] - 1]:
		return False
	visited[pos[0] - 1][pos[1] - 1] = True
	reachable = []
	if (pos[0]) * (pos[1]) in coords:
		reachable = coords[(pos[0]) * (pos[1])]
	return any([room_bfs(npos) for npos in reachable])

print("yes" if room_bfs((M, N)) else "no")
