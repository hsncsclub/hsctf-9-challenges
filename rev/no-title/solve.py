match = [
	119, 113, 215, 125, 223, 163, 121, 211, 127, 231, 223, 111, 197, 209, 163, 215, 195, 197, 193, 117, 209, 211, 235, 223, 117, 209
]
indicies = [
	7, 18, 2, 5, 16, 1, 3, 14, 6, 13, 21, 12, 4, 17, 9, 10, 19, 24, 20, 11, 25, 22, 15, 23, 0, 8
]

x = [((((v - 1) ^ 23) - 1) // 2) ^ 5 for v in match]

for i, index in reversed(list(enumerate(indicies))):
	x[index], x[i] = x[i], x[index]

print(bytes(reversed(x)).decode())
