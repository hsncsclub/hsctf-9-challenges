import random

flag = open('flag.txt', 'r').read()

min_coin = 5000
max_coin = 20000
num_coins = 19
closeness = int(0.05 * max_coin)
min_split = 3
max_split = 4

coins = []
for i in range(num_coins):
	coins += [random.randint(min_coin, max_coin)]

items = []
ptr = 0
while ptr < num_coins:
	split = random.randint(min_split, max_split)
	cur = 0
	for j in range(ptr, min(ptr + split, num_coins)):
		cur += coins[j]
	cur -= random.randint(0, closeness)
	ptr += split
	items += [cur]

random.shuffle(items)
random.shuffle(coins)
num_items = len(items)

used_items = [False] * num_items
used_coins = [False] * num_coins
balance = 0

def disp():
	print("Items: ")
	for i in range(num_items):
		if used_items[i]:
			continue
		print(str(i + 1) + ": " + str(items[i]))
	print("\nCoins: ")
	for i in range(num_coins):
		if used_coins[i]:
			continue
		print(str(i + 1) + ": " + str(coins[i]))
	print("\nBalance: " + str(balance))

def insert(x, balance):
	x -= 1
	if x >= num_coins or x < 0:
		print("Out of Range")
	elif used_coins[x]:
		print("Coin does not exist")
	else:
		used_coins[x] = True
		balance += coins[x]
		print("Balance: " + str(balance))
	return balance

def buy(x, balance):
	x -= 1
	if x >= num_items or x < 0:
		print("Out of Range")
	elif used_items[x]:
		print("Item does not exist")
	elif items[x] > balance:
		print("Not enough money")
	else:
		used_items[x] = True
		balance = 0
		print("Balance: " + str(balance))
	return balance

def done():
	for x in used_items:
		if not x:
			return False
	return True

while True:
	query = input()
	try:
		splt = query.split()
		if splt[0] == "Buy":
			balance = buy(int(splt[1]), balance)
		elif splt[0] == "Insert":
			balance = insert(int(splt[1]), balance)
		elif splt[0] == "Display":
			disp()
		else:
			print("Bad Input")
	except:
		print("Bad Input")
	if done():
		print(flag)
		break

