inp = input()
vals = inp.split()
N = int(vals[0])
M = int(vals[1])
K = int(vals[2])
res = []

for i in range(N):
	spots_left = N - i - 1
	cur_val = K - spots_left
	choice = min(cur_val, M)
	if choice <= 0:
		break

	if choice > i:
		val = min(M, i + 1)
		choice = val

	else:
		val = res[i - choice]

	res.append(str(val))
	K -= choice

if K == 0 and len(res) == N:
	print(' '.join(res))
else:
	print("-1")
