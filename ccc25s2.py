import re

code = input()
c = int(input())
codeints = [int(n) for n in re.findall(r"\d+", code)]
reallen = sum(codeints)
codechars = re.findall("[a-z]", code)

cidx = c % reallen
curidx = 0

for idx, (codeint, codechar) in enumerate(zip(codeints, codechars)):
	curidx += codeint
	if curidx > cidx:
		print(codechar)
		break
