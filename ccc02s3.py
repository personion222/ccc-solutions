r = int(input())
c = int(input())

grid = []
for _ in range(r):
    grid.append(list(input()))

m = int(input())
path = [(0, 0)]
direction = (-1, 0)
for _ in range(m):
    move = input()
    if move == 'F':
        path.append((path[-1][0] + direction[0], path[-1][1] + direction[1]))

    if move == 'L':
        if direction == (-1, 0):
            direction = (0, -1)
        elif direction == (0, -1):
            direction = (1, 0)
        elif direction == (1, 0):
            direction = (0, 1)
        else:
            direction = (-1, 0)

    else:
        if direction == (0, -1):
            direction = (-1, 0)
        elif direction == (1, 0):
            direction = (0, -1)
        elif direction == (0, 1):
            direction = (1, 0)
        else:
            direction = (0, -1)

print(path)
