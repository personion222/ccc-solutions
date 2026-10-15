import sys
sys.setrecursionlimit(100000)

n = int(input())

def bfs(current, end, depth=-1):
    global seen
    if current == end:
        return depth
    branches = friends[current]
    mindepth = float("inf")
    for branch in branches:
        if branch not in seen:
            seen.add(branch)
            branch_depth = bfs(branch, end, depth + 1)
            if branch_depth < mindepth:
                mindepth = branch_depth

    return mindepth

friends = {}

for _ in range(n):
    f1, f2 = [int(f) for f in input().split()]
    if f1 in friends:
        friends[f1].append(f2)
    else:
        friends[f1] = [f2]

out = []

check = [int(f) for f in input().split()]
while 1:
    seen = set()
    if check == [0, 0]:
        break
    check_depth = bfs(check[0], check[1])
    if check_depth == float("inf"):
        out.append("No")
    else:
        out.append(f"Yes {check_depth}")
    check = [int(f) for f in input().split()]

print('\n'.join(out))
