try:
	age = int(input('How old are you? '))
except ValueError:
	print('Please write your age with a numerical value such as 15.')
	age = int(input('How old are you? '))

if age > 18:
	print('You are an adult.')

