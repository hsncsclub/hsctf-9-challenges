import random
from math import sqrt
print("c")
from numpy.random import normal
print("yuh")
from Crypto.Util.number import bytes_to_long

def secure_seed():
	return int(normal(25000000000, 1000000/sqrt(18)))

print("a")
flag = open('flag.txt','rb').read()
print(flag)
flag = bytes_to_long(flag)

s = secure_seed()
print(s)
random.seed(s)

l = len(bin(flag)) - 1
print(l)

k = random.getrandbits(l)
flag = flag ^ k # super secure encryption
print(flag)

