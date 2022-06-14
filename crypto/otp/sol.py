import random

f = open('output.txt', 'r')
bits = int(next(f))
c = int(next(f))
mean = 25000000000
for i in range(2000000):
	n = mean
	if (i % 2) == 1:
		n += i//2
	else:
		n -= i//2
	random.seed(n)
	k = random.getrandbits(bits)
	flag = c ^ k
	flag = flag.to_bytes((bits-1+7)//8, 'big')
	if flag[0:5] == 'flag{'.encode('utf-8'):
		print(flag)
