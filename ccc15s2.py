j = int(input())
a = int(input())
js = []
for i in range(j):
	size = input()
	if size == 'S':
		js.append(0)

	if size == 'M':
		js.append(1)

	if size == 'L':
		js.append(2)

max_reqs = 0
taken = set()
for k in range(a):
	size_str, no = input().split()
	if size_str == 'S':
		size = 0

	if size_str == 'M':
		size = 1

	if size_str == 'L':
		size = 2

	if js[int(no) - 1] >= size and int(no) - 1 not in taken:
		taken.add(int(no) - 1)
		max_reqs += 1

print(max_reqs)
