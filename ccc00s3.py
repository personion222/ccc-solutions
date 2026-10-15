n = int(input())
pages = {}
lines = []

while 1:
	line = input()
	if len(line) > 6:
		if line[:6] == "<HTML>":
