m = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
A = int(input())
B = int(input())
N = int(input())
for _ in range(N):
	m.append(int(input()))
m.sort()
def get_reachable(idx):
	if idx == 0:
		return True

	pos = m[idx]
	reachables = list()
	nextidx = idx
	while nextidx >= 0 or A < (pos - m[nextidx]) < B:
		nextidx -= 1
		reachables.append(nextidx)



	return [get_reachable(x) for x in reachables]

print(get_reachable(len(m) - 1))
