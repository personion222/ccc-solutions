t = int(input())
out = []
for i in range(t):
    n = int(input())
    cars = []
    for j in range(n):
        cars.append(int(input()))
    cars = cars[::-1]

    declast = n + 1
    inclast = 0
    exiting = False
    for car in cars:
        if declast - car != 1:
            if car - inclast != 1:
                exiting = True
                break
            else:
                inclast = car
        else:
            declast = car
    if exiting:
        out.append('N')
        continue
    out.append('Y')

print('\n'.join(out))
