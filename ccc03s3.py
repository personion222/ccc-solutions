f = int(input())
r = int(input())
c = int(input())

house = [input().split() for _ in range(r)]


def ff(row_idx, col_idx, visited=[]):
	if row_idx > 0:
		if house[row_idx - 1][col_idx] == '.' and (row_idx - 1, col_idx) not in visited:
			return ff(row_idx - 1, col_idx, visited + [(row_idx, column_idx)])
	if col_idx > 0:
		if house[row_idx][col_idx - 1] == '.' and (row_idx, col_idx - 1) not in visited:
			return ff(row_idx - 1, col_idx, visited + [(row_idx, column_idx)])
	if row_idx < r - 1:
		if house[row_idx + 1][col_idx] == '.' and (row_idx + 1, col_idx) not in visited:
			return ff(row_idx - 1, col_idx, visited + [(row_idx, column_idx)])
	if col_idx < c - 1:
		if house[row_idx][col_idx + 1] == '.' and (row_idx, col_idx + 1) not in visited:
			return ff(row_idx - 1, col_idx, visited + [(row_idx, column_idx)])

	return visited + [(row_idx, column_idx)]


rooms_tiles = {}
room_areas = []

for row_idx, row in enumerate(house):
	for col_idx, tile in enumerate(house):
		if tile == '.' and (row_idx, col_idx) not in rooms_tiles:
			room_tiles = ff(row_idx, col_idx)
			for room_tile in room_tiles:
				rooms_tiles.add(room_tile)
			room_areas.append(len(room_tiles))

print(room_areas)
