import random
from collections import Counter

flag = open('flag.txt', 'r').read()

n_list = [4, 10, 30, 50, 50]
low = 10
high = 100

good = True

for n in n_list:
	a = random.sample(range(low, high), n)
	print(a)
	ans = max(a)*2
	order = input("order: ")
	order = order.split()
	order = list(map(int, order))
	if Counter(order) != Counter(a):
		print("Bad input")
		good = False
		break
	ptr = 0
	dist = 0
	for x in order:
		dist += abs(x - ptr)
		ptr = x
	dist += ptr
	if dist != ans:
		print("Distance too large")
		good = False
		break

if good:
	print(flag)
