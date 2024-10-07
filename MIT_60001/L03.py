####################
## Index and Slice
####################
# s = "abc"
# s[0] evaluates to "a"
# s[1] evaluates to "b"
# s[2] evaluates to "c"
# s[3] trying to index out of bounds, error
# s[-1] evaluates to "c"
# s[-2] evaluates to "b"
# s[-3] evaluates to "a"

# s = "abcdefgh"
# s[3:6] evaluates to "def", same as s[3:6:1]
# s[3:6:2] evaluates to "df"
# s[::] evaluates to "abcdefgh", same as s[0:len(s):1]
# s[::-1] evaluates to "hgfedbca", same as s[-1:-(len(s)+1):-1]
# s[4:1:-2] evaluates to "ec"

# strings are “immutable” – cannot be modified
# s = "hello"
# s[0] = 'y' gives an error
# s = 'y'+ s[1:len(s)] is allowed,
# s bound to new object

####################
## EXAMPLE: for loops over strings
####################
s = "demo loops"
for index in range(len(s)):
   if s[index] == 'i' or s[index] == 'u':
	   print("There is an i or u")

for char in s:
   if char == 'i' or char == 'u':
	   print("There is an i or u")


####################
## EXAMPLE: while loops and strings
## CHALLENGE: rewrite while loop with a for loop
####################
an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

i = 0
while i < len(word):
	char = word[i]
	if char in an_letters:
		print("Give me an " + char + "! " + char)
	else:
		print("Give me a  " + char + "! " + char)
	i += 1

for char in word:
	if char in an_letters:
		print("Give me an " + char + "! " + char)
	else:
	 	print("Give me a  " + char + "! " + char)
	
print("What does that spell?")
for i in range(times):
   print(word, "!!!")

##### ALGORITHMS ######
	
####################
## EXAMPLE: perfect cube 
####################
#cube = 27
##cube = 8120601
#for guess in range(cube+1):
#    if guess**3 == cube:
#        print("Cube root of", cube, "is", guess)
#        # loops keeps going even after found the cube root
	

####################
## EXAMPLE: guess and check cube root 
####################
cube = 27
#cube = 8120601
for guess in range(abs(cube)+1):
   # passed all potential cube roots
   if guess**3 >= abs(cube):
       # no need to keep searching
       break
if guess**3 != abs(cube):
   print(cube, 'is not a perfect cube')
else:
   if cube < 0:
       guess = -guess
   print('Cube root of ' + str(cube) + ' is ' + str(guess))


####################
## EXAMPLE: approximate cube root 
####################
cube = 27
#cube = 8120601
# cube = 10000
epsilon = 0.1 # how far we are from the answer
guess = 0.0
increment = 0.01
num_guesses = 0
# look for close enough answer and make sure
# didn't accidentally skip the close enough bound
# while abs(guess**3 - cube) >= epsilon and guess**3 <= cube: # I tried becaus eit was more logic
while abs(guess**3 - cube) >= epsilon and guess**3 <= cube:
#    if guess > 9999.5:
#         print("guess: ", guess)
#         print("cube: ", cube)
   guess += increment
   num_guesses += 1
print('num_guesses =', num_guesses)
# print("guess: ", guess)
# print("cube: ", cube)
if abs(guess**3 - cube) >= epsilon:
   print('Failed on cube root of', cube, "with these parameters.")
else:
   print(guess, 'is close to the cube root of', cube)


####################
## EXAMPLE: bisection cube root (only positive cubes!)
####################
cube = 27
#cube = 8120601
cube = 0.25
epsilon = 0.01
num_guesses = 0
# won't work with x < 1 because initial upper bound is less than ans
# so that if statement is written
if cube < 1:
     low = cube
     high = 1
else:
     low = 0
     high = cube
guess = (high + low)/2.0
# if cube < 1: # one line solves it she said !
     
while abs(guess**3 - cube) >= epsilon:
   if guess**3 < cube:
       # look only in upper half search space
       low = guess
   else:
       # look only in lower half search space
       high = guess
   # next guess is halfway in search space
   guess = (high + low)/2.0
   num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)
   