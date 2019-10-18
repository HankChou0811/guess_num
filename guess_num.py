import random

r = random.randint(1, 100)
while True:
	num = input('please guess number: ')
	num = int(num)
	if num == r:
		print('THATS RIGHT!!!')
		break
	elif num > r:
		print('it is larger than the actual number')
	elif num < r:
		print(' it is smaller than the actual number')
	else:
		print('???')
