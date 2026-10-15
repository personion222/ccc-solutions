N = int(input())
L = [int(x) for x in input().split()]

pair_sums = {}

for x in range(len(L)):
	for y in range(x + 1, len(L)):
		print(L[x], L[y])

		if L[x] + L[y] in pair_sums:
			pair_sums[L[x] + L[y]] += 1
		else:
			pair_sums[L[x] + L[y]] = 1
