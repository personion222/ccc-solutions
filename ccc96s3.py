from itertools import combinations

num_pairs = int(input())
pairs = [[int(x) for x in input().split()] for _ in range(num_pairs)]

for idx, pair in enumerate(pairs):
	patterns = []
	index_sets = combinations(range(pair[0]), pair[1])

	for index_set in index_sets:
		patterns.append(['0'] * pair[0])
		for index in index_set:
			patterns[-1][index] = '1'
		patterns[-1] = ''.join(patterns[-1])

	print("The bit patterns are")
	for pattern in patterns:
		print(pattern)
	if idx < len(pairs) - 1:
		print()
