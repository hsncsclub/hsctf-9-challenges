from random import SystemRandom

flag = open('flag.txt', 'r').read()

gen = SystemRandom()
numTrials = 200
p = .935
n = 8

correct = 0

for i in range(numTrials):
	cur = gen.randint(1, n)
	print("Trial " + str(i + 1) + ":")
	for j in range(n):
		guess = input("guess: ")
		if int(guess) == cur:
			print("correct")
			correct += 1
			break
		else:
			print("incorrect")
		if cur == 1:
			cur = 2
		elif cur == n:
			cur = n-1
		elif gen.randint(0, 1) == 0:
			cur -= 1
		else:
			cur += 1

print("You won in " + str(correct) + " out of " + str(numTrials) + " trials")
if correct >= p * numTrials:
	print(flag)
else:
	print("better luck next time!")

