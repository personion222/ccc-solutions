N = int(input())
frequencies = {}

for _ in range(N):
	R = int(input())
	if R in frequencies:
		frequencies[R] += 1
	else:
		frequencies[R] = 1

max_freq = 0
max_freq_vals = []
max2_freq = 0
max2_freq_vals = []

for value, frequency in frequencies.items():
	if frequency > max_freq:
		max2_freq = max_freq
		max2_freq_vals = max_freq_vals.copy()
		max_freq = frequency
		max_freq_vals = [value]

	elif frequency == max_freq:
		max_freq_vals.append(value)

	elif frequency > max2_freq:
		max2_freq = frequency
		max2_freq_vals = [value]

	elif frequency == max2_freq:
		max2_freq_vals.append(value)

# print(max_freq_vals)

if len(max_freq_vals) >= 2:
	print(abs(max(max_freq_vals) - min(max_freq_vals)))

else:
	print(max(abs(max_freq_vals[0] - min(max2_freq_vals)), abs(max_freq_vals[0] - max(max2_freq_vals))))
