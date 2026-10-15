q = int(input())
ans = []
for _ in range(q):
	ans.append(input())
s = 0
for i in range(q):
	if input() == ans[i]:
		s += 1

print(s)
