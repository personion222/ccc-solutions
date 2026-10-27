from copy import deepcopy

t = int(input())

tests = []

for _ in range(t):
    n = int(input())
    tests.append([int(input()) for __ in range(n)])

out = []

for test in tests:
    highest = len(test)
    lowest = 1
    branch = []
    lake = []
    test_cars = deepcopy(test)
    result = 'Y'
    while test_cars:
        if test_cars[-1] == lowest:
            lowest += 1
            lake.append(test_cars.pop())
        elif branch:
            if test_cars[-1] < branch[-1]:
                branch.append(test_cars.pop())
        else:
            result = 'N'
            break
    if result == 'Y':
        if not all([lake[i] < lake[i + 1] for i in range(len(lake) - 1)]):
            result = 'N'

    out.append(result)

print('\n'.join(out))
