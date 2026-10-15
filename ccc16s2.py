ismax = input() == '2'
cit = int(input())
dcits = sorted([int(x) for x in input().split()], reverse=False)
pcits = sorted([int(y) for y in input().split()], reverse=ismax)

pairs = []
for _ in range(cit):
	pairs.append((dcits.pop(0), pcits.pop(0)))

# print(pairs)

print(sum([max(x, y) for x, y in pairs]))
