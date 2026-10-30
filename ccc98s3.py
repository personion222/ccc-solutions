def turn(src, dst):
	left_dist = 0
	right_dist = 0
	cur = src
	while cur != dst:
		left_dist += 1
		cur = left_turn[cur]
	cur = src
	while cur != dst:
		right_dist += 1
		cur = right_turn[cur]
	if left_dist < right_dist:
		return ['3'] * left_dist
	return ['2'] * right_dist

n = int(input())

right_turn = {
	(1, 0): (0, 1),
	(0, 1): (-1, 0),
	(-1, 0): (0, -1),
	(0, -1): (1, 0)
}
left_turn = {val: key for key, val in right_turn.items()}
excursions = []
end_directions = []

for _ in range(n):
	excursions.append([(0, 0)])
	direction = (1, 0)
	while 1:
		command = int(input())
		if command == 0:
			end_directions.append(direction)
			break
		elif command == 1:
			mag = int(input())
			excursions[-1].append((excursions[-1][-1][0] + direction[0] * mag, excursions[-1][-1][1] + direction[1] * mag))
			continue
		elif command == 2:
			direction = right_turn[direction]
		else:
			direction = left_turn[direction]

for idx, excursion in enumerate(excursions):
	print(f"Distance is {abs(excursion[-1][0]) + abs(excursion[-1][1])}")

	if excursion[-1] != (0, 0):
		if excursion[-1][0] == 0:
			print('\n'.join(turn(end_directions[idx], (0, excursion[-1][1] // -abs(excursion[-1][1])))))
			print(f"1\n{abs(excursion[-1][1])}")
		elif excursion[-1][1] == 0:
			print('\n'.join(turn(end_directions[idx], (excursion[-1][0] // -abs(excursion[-1][0]), 0))))
			print(f"1\n{abs(excursion[-1][0])}")
		else:
			x_dir = (excursion[-1][0] // -abs(excursion[-1][0]), 0)
			y_dir = (0, excursion[-1][1] // -abs(excursion[-1][1]))
			xy_turns = len(turn(end_directions[idx], x_dir)) + len(turn(x_dir, y_dir))
			yx_turns = len(turn(end_directions[idx], y_dir)) + len(turn(y_dir, x_dir))
			if xy_turns < yx_turns:
				if turn(end_directions[idx], x_dir):
					print('\n'.join(turn(end_directions[idx], x_dir)))
				print(f"1\n{abs(excursion[-1][0])}")
				if turn(x_dir, y_dir):
					print('\n'.join(turn(x_dir, y_dir)))
				print(f"1\n{abs(excursion[-1][1])}")
			else:
				if turn(end_directions[idx], y_dir):
					print('\n'.join(turn(end_directions[idx], y_dir)))
				print(f"1\n{abs(excursion[-1][1])}")
				if turn(y_dir, x_dir):
					print('\n'.join(turn(y_dir, x_dir)))
				print(f"1\n{abs(excursion[-1][0])}")

	if idx < len(excursions) - 1:
		print()
