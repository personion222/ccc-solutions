def is_heavy_light(string):
	occs = {}
	for char in string:
		if char in occs:
			occs[char] += 1
		else:
			occs[char] = 1

	last = occs[string[0]] > 1
	for char in string[1 :]:
		if (occs[char] > 1) != last:
			last = occs[char] > 1
		else:
			return False

	return True

count, length = list(map(int, input().split()))

strs = []
for _ in range(count):
	strs.append(input())

for string in strs:
	print('T' if is_heavy_light(string) else 'F')
