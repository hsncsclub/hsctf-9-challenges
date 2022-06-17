import random

flag = open('flag.txt', 'r').read()

min_coin = 40000
max_coin = 50000
num_coins = 200
closeness = int(0.0001 * max_coin)
splits = [4] * 36 + [3] * 16 + [2] * 4
num_trials = 12
correct = 0

for i in range(num_trials):
	print("Machine " + str(i + 1) + ":")
	coins = []
	for i in range(num_coins):
		coins += [random.randint(min_coin, max_coin)]

	items = []
	ptr = 0
	for split in splits:
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
				for u in splt[1:]:
					balance = insert(int(u), balance)
			elif splt[0] == "Display":
				disp()
			else:
				print("Bad Input")
		except:
			print("Bad Input")
		if done():
			correct += 1
			break
if correct == num_trials:
	print(flag)
