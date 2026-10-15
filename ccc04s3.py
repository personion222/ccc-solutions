from sys import setrecursionlimit
setrecursionlimit(10 ** 6)


def charnum2coord(charnum: str):
	'''turn a character number sequence (e.g. A1) into a zero indexed coordinate (y, x)'''
	return ord(charnum[0]) - 65, int(charnum[-1]) - 1

def is_cyclic(graph, coord, visited):
	# print(coord, visited)
	if coord in visited:
		return True

	node_content = graph[coord[0]][coord[1]]

	if isinstance(node_content, int):
		return False

	return any([is_cyclic(graph, linked_node, visited | {node_content}) for linked_node in node_content])


spreadsheet = []
sums = set()
to_calc = set()
cyclics = set()

output = [['' for __ in range(9)] for _ in range(10)]

for y in range(10):
	row = input().split()
	spreadsheet.append([])
	for x, col in enumerate(row):
		if col.isnumeric():
			spreadsheet[-1].append(int(col))
			output[y][x] = col
		else:
			spreadsheet[-1].append(tuple(map(charnum2coord, col.split('+'))))
			sums.add((y, x))

for y, x in sums:
	if is_cyclic(spreadsheet, (y, x), {(y, x)}):
		output[y][x] = '*'
		cyclics.add((y, x))
	else:
		to_calc.add((y, x))

while to_calc:
	rmed = []
	for y, x in to_calc:
		included_vals =
		if all([isinstance(spreadsheet[ay][ax], int) for ay, ax in spreadsheet[y][x]]):
			spreadsheet[y][x] = sum([spreadsheet[ay][ax] for ay, ax in spreadsheet[y][x]])
			output[y][x] = str(spreadsheet[y][x])
			# print(to_calc)
			rmed.append((y, x))

	for rm in rmed:
		to_calc.remove(rm)

print(spreadsheet)
print(all([isinstance(spreadsheet[ay][ax], int) for ay, ax in spreadsheet[0][3]]))
print(sum([spreadsheet[ay][ax] for ay, ax in spreadsheet[y][x]]))
print('\n'.join([' '.join(row) for row in output]))

'''
1 2 3 A1+A2+A3 A3+A4 A1+A4+A5 A8+A9 A9 A8
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
1 2 3 J1+J2+J5 J3+J4 A1+A4+A5 A8+A9 J9 J8
'''
