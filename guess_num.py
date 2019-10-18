import random

r = random.randint(1, 100)
count = 0
while True:
	count = count + 1 # same as "count += 1"
	num = input('please guess number: ')
	num = int(num)
	if num == r:
		print('THATS RIGHT!!!')
		print('it is', count , 'times you guessing')
		break
	elif num > r:
		print('guess a smaller one')
	elif num < r:
		print(' guess a larger one')
	else:
		print('???')
	print('it is', count , 'times you guessing')
