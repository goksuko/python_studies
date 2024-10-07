# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:52:34 2016

@author: WELG
"""

def multi_iter(a, b):
	result = 0
	while b > 0:
		result = result + a
		b -= 1
	return result

print(multi_iter(5, 3))

def mult(a, b):
	if b == 1:
		return a
	return a + mult(a, b - 1)
	
print(mult(5, 3))

def fact(x):
	if x == 1:
		return 1
	else:
		return x * fact(x - 1)
	
print(fact(5)) # x is not changed, is not mutated in the frames of recursion, 
# so we are literally creating a local scope for that recursive call
# you dont have to think about interior variables

def fact_iter(x):
	res = 1
	for i in range (1, x+1):
		res *= i
	return res

print(fact_iter(5))

#####################################
# EXAMPLE:  Towers of Hanoi
#####################################

def printMove(fr, to): # from, to, spare
	print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
	if n == 1:
		printMove(fr, to)
	else:
		Towers(n-1, fr, spare, to) # take n-1 from from to spare
		Towers(1, fr, to, spare) # take 1 from from to to
		Towers(n-1, spare, to, fr) # take that n-1 from spare to to

# print(Towers(4, 'P1', 'P2', 'P3'))

# I wrote below : yeayyyy

def fibo(x):
	if x == 0:
		return 1
	elif x == 1:
		return 1
	elif x == 2:
		return 2
	else:
		return fibo(x - 1) + fibo(x - 2)
	
print(fibo(25))

#####################################
# EXAMPLE:  fibonacci
#####################################

def fib(x):
	"""assumes x an int >= 0
	   returns Fibonacci of x"""
	if x == 0 or x == 1:
		return 1
	else:
		return fib(x-1) + fib(x-2)
	
print(fib(25))

# my_trial but not works well

# def is_pal(str):

# 	def toChars(s):
# 		s = s.lower()
# 		ans = ''
# 		for c in s:
# 			if c in 'abcdefghijklmnopqrstuvwxyz':
# 				ans = ans + c
# 		return ans
	
# 	str = str.lower()
# 	str = toChars(str)
# 	# print("str:", str)
# 	length = len(str)

# 	if len(str) == 1:
# 		return True
# 	elif len(str) == 2 and str[0] == str[1]:
# 		return True
# 	elif len(str) == 2 and str[0] != str[1]:
# 		return False
# 	else:
# 		for n in range(1, len(str) // 2 + 1):
# 			return is_pal(str[n:length - n])
		
# print(is_pal('eve'))

# print(is_pal('Able was I, ere I saw Elba'))

# print(is_pal('Is this a palindrome'))

# print()

#####################################
# EXAMPLE:  testing for palindromes
#####################################
		
def isPalindrome(s):

	def toChars(s):
		s = s.lower()
		ans = ''
		for c in s:
			if c in 'abcdefghijklmnopqrstuvwxyz':
				ans = ans + c
		return ans

	def isPal(s):
		if len(s) <= 1:
			return True
		else:
			return s[0] == s[-1] and isPal(s[1:-1])

	return isPal(toChars(s))

print(isPalindrome('eve'))

print(isPalindrome('Able was I, ere I saw Elba'))

print(isPalindrome('Is this a palindrome'))

#####################################
# EXAMPLE: using dictionaries
#          counting frequencies of words in song lyrics
#####################################

#### DICTIONARIES
# keys are immutable but other values can be mutable data types
# keys can be added or deleted (with everything inside)
# keys can be ints, floats, strings, tuples, booleans :> any immutable type
# keys are not oredered!


def lyrics_to_frequencies(lyrics):
	myDict = {}
	for word in lyrics:
		word = word.lower()
		if word in myDict:
			myDict[word] += 1
		else:
			myDict[word] = 1
	return myDict
	
	
she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 
'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

'you', 'think', "you've", 'lost', 'your', 'love',
'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
"it's", 'you', "she's", 'thinking', 'of',
'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'she', 'said', 'you', 'hurt', 'her', 'so',
'she', 'almost', 'lost', 'her', 'mind',
'and', 'now', 'she', 'says', 'she', 'knows',
"you're", 'not', 'the', 'hurting', 'kind',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',

'you', 'know', "it's", 'up', 'to', 'you',
'i', 'think', "it's", 'only', 'fair',
'pride', 'can', 'hurt', 'you', 'too',
'pologize', 'to', 'her',

'Because', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'yeah', 'yeah', 'yeah',
'yeah', 'yeah', 'yeah', 'yeah'
]

beatles = lyrics_to_frequencies(she_loves_you)

print("\nlyrics dictionary:", beatles, "\n")


def most_common_words(freqs):
	values = freqs.values()
	best = max(freqs.values())
	# print("best:", best, "\n")
	words = []
	for k in freqs:
		if freqs[k] == best:
			words.append(k)
	return (words, best)
	
def words_often(freqs, minTimes):
	result = []
	done = False
	while not done:
		temp = most_common_words(freqs)
		if temp[1] >= minTimes:
			result.append(temp)
			for w in temp[0]:
				# print("to be deleted:", freqs[w])
				del(freqs[w])  #remove word from dict
		else:
			done = True
	return result
	
print(words_often(beatles, 5), "\n")

#####################################
# EXAMPLE: comparing fibonacci using memoization
#####################################


def fib(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		return fib(n-1) + fib(n-2)


def fib_efficient(n, d):
	if n in d:
		return d[n]
	else:
		ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
		d[n] = ans
		return ans
		
d = {1:1, 2:2}

argToUse = 34
print("")
print('using fib')
print(fib(argToUse))
print("")
print('using fib_efficient')
print(fib_efficient(argToUse, d))