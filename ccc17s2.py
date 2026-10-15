n = int(input())
measurements = sorted(list(map(int, input().split())))
if n % 2 == 1:
	lows = measurements[: n // 2 + 1]
	highs = measurements[n // 2 + 1 :]
else:
	lows = measurements[: n // 2]
	highs = measurements[n // 2 :]

out = []
while lows or highs:
	try:
		out.append(str(lows.pop(-1)))
	except IndexError:
		pass
	try:
		out.append(str(highs.pop(0)))
	except IndexError:
		pass

print(' '.join(out))
