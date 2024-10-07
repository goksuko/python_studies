from typing import List

class Solution:
	def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
		if len(sentence1) > len(sentence2): 
			temp = sentence1
			sentence1 = sentence2
			sentence2 = temp
		#sen1 short #sen2 long
		length = list(sentence1)
		sen1 = sentence1.list()
		print(sen1)
		print("length:", length)
		i = 0
		j = 0
		for c in sentence2[j]:
			print(c)
			if c in sentence1[i]:
				i += 1
				print(c)
			elif i == length or i == length + 1:
				return True
			else:
				i = 0
			j += 1
		print(i)
		return False

#below is not fully correct
	def areSentencesSimilar2(self, sentence1: str, sentence2: str) -> bool:
		# sentence1 = sentence1.lower()
		# sentence2 = sentence2.lower()
		list1 = sentence1.split()
		list2 = sentence2.split()
		same1 = False
		dif1 = False
		same2 = False
		dif2 = False
		same3 = False
		i1 = 0
		i2 = 0
		while 1:
			while len(list1) != i1 and len(list2) != i2 and list1[i1] == list2[i2]:
				i1 += 1
				i2 += 1
				same1 = True
			print("Same1:", same1)
			while len(list1) != i1 and len(list2) != i2 and list1[i1] != list2[i2]:
				if len(list1) > len(list2):
					i1 += 1
				else:
					i2 += 1
				dif1 = True
			print("Dif1:", dif1)
			while len(list1) != i1 and len(list2) != i2 and list1[i1] == list2[i2]:
				i1 += 1
				i2 += 1
				same2 = True
			print("Same2:", same2)
			while len(list1) != i1 and len(list2) != i2 and list1[i1] != list2[i2]:
				if len(list1) > len(list2):
					i1 += 1
				else:
					i2 += 1
				dif2 = True
			if len(list1) != i1 or len(list2) != i2:
				dif2 = True
			print("Dif2:", dif2)
			while len(list1) != i1 and len(list2) != i2 and list1[i1] == list2[i2]:
				i1 += 1
				i2 += 1
				same3 = True
			print("Same3:", same3)
			if (dif1 and dif2):
				return False
			elif (dif1 or dif2) and (same1 and same3):
				return False
			elif (dif1 or dif2):
				return True
			elif (dif1 == False and dif2 == False):
				return True
			elif (len(list1) == i1 and len(list2) == i2):
				return True
			else:
				return False

		
sol = Solution()

ans = sol.areSentencesSimilar("xD iP tqchblXgqvNVdi", "FmtdCzv Gp YZf UYJ xD iP tqchblXgqvNVdi")
print("True", ans, "\n")	
ans = sol.areSentencesSimilar("of", "A lot of words")
print("False", ans, "\n")
ans = sol.areSentencesSimilar("Hello Jane", "Hello my name is Jane")
print("True", ans, "\n")
ans = sol.areSentencesSimilar("Eating right now", "Eating")
print("True", ans, "\n")
ans = sol.areSentencesSimilar("A", "a A b A")
print("True", ans, "\n")


# 1813. Sentence Similarity III
# Medium

# You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.

# Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. Note that the inserted sentence must be separated from existing words by spaces.

# For example,

# s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in s1.
# s1 = "Frog cool" and s2 = "Frogs are cool" are not similar, since although there is a sentence "s are" inserted into s1, it is not separated from "Frog" by a space.
# Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.

 

# Example 1:

# Input: sentence1 = "My name is Haley", sentence2 = "My Haley"

# Output: true

# Explanation:

# sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".

# Example 2:

# Input: sentence1 = "of", sentence2 = "A lot of words"

# Output: false

# Explanation:

# No single sentence can be inserted inside one of the sentences to make it equal to the other.

# Example 3:

# Input: sentence1 = "Eating right now", sentence2 = "Eating"

# Output: true

# Explanation:

# sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.

 

# Constraints:

# 1 <= sentence1.length, sentence2.length <= 100
# sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
# The words in sentence1 and sentence2 are separated by a single space.