n = int(input())
teams = [int(input()) for _ in range(n)]

for idx, t in enumerate(teams):
	rounds = 0
	undefeated_ct = t
	oneloss_ct = 0
	elim_ct = 0
	print(f"Round {rounds}: {undefeated_ct} undefeated, {oneloss_ct} one-loss, {elim_ct} eliminated")

	while undefeated_ct + oneloss_ct > 1:
		if undefeated_ct + oneloss_ct > 2:
			undefeated_pairs = undefeated_ct // 2
			oneloss_pairs = oneloss_ct // 2
			undefeated_ct -= undefeated_pairs
			oneloss_ct -= oneloss_pairs
			oneloss_ct += undefeated_pairs
			elim_ct += oneloss_pairs
		else:
			if undefeated_ct == 2:
				undefeated_ct = 1
				oneloss_ct = 1
			elif undefeated_ct == 1:
				undefeated_ct = 0
				oneloss_ct = 2
			else:
				oneloss_ct = 1
				elim_ct += 1
		rounds += 1
		print(f"Round {rounds}: {undefeated_ct} undefeated, {oneloss_ct} one-loss, {elim_ct} eliminated")

	print(f"There are {rounds} rounds.")

	if idx != len(teams) - 1:
		print()
