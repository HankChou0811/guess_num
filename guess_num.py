import random
start = input('please make a inital number: ')
end = input('please make a ending number: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
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
