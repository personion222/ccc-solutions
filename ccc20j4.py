T = input()
S = input()
yes = False
# ABCDE
for shift in range(len(S)):
	sub = S[shift:] + S[0:shift % len(S)]
	if sub in T:
		yes = True
		break
print("yes" if yes else "no")
