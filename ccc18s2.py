def rotarr(arr):
	rot = [[] for _ in range(len(arr))]
	for r, row in enumerate(arr):
		for c, val in enumerate(row):
			rot[len(arr) - c - 1].append(val)
	return rot

def check_rows(arr):
	for row in inarr:
		for idx, val in enumerate(row):
			if idx > 0:
				if val < row[idx - 1]:
					return False
	return True

def check_cols(arr):
	for colidx in range(len(arr)):
		for rowidx in range(len(arr)):
			if rowidx > 0:
				if arr[rowidx][colidx] < arr[rowidx - 1][colidx]:
					return False
	return True


N = int(input())
inarr = [[int(x) for x in input().split()] for _ in range(N)]

while True:
	if check_rows(inarr):
		if check_cols(inarr):
			break
	inarr = rotarr(inarr)
	# print(inarr)

print('\n'.join([' '.join([str(val) for val in row]) for row in inarr]))
