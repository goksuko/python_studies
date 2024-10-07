### compund data types ###
# because they are made up of other data types
# like ints, floats, blooeans, characters, strings, lists, tuples, and dictionaries
# 1. Tuples
# 2. Lists

## Tuples
# Tuples are ordered sequences of elements
# Tuples are immutable - not allowed to change the elements

#########################
## EXAMPLE: returning a tuple
#########################
def quotient_and_remainder(x, y):
    q = x // y # integer division so 0
    r = x % y # remainder is 4
    return (q, r)
    
(quot, rem) = quotient_and_remainder(4, 5)
print("quot:", quot)
print("rem:", rem, "\n")


#########################
## EXAMPLE: iterating over tuples
#########################
def get_data(aTuple):
    """
    aTuple, tuple of tuples (int, string)
    Extracts all integers from aTuple and sets 
    them as elements in a new tuple. 
    Extracts all unique strings from from aTuple 
    and sets them as elements in a new tuple.
    Returns a tuple of the minimum integer, the
    maximum integer, and the number of unique strings
    """
    nums = ()    # empty tuple
    words = ()
    for t in aTuple:
        # concatenating with a singleton tuple
        nums = nums + (t[0],)   
        # only add words haven't added before
        if t[1] not in words:   
            words = words + (t[1],)
        print("nums:", nums, "\nwords:", words, "\n")
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

test = ((1,"a"),(2, "b"),
        (1,"a"),(7,"b"))
(a, b, c) = get_data(test)
print("min:",a,"max:",b,"uniq word no:",c, "\n")

# apply to any data you want!
tswift = ((2014,"Katy"),
          (2014, "Harry"),
          (2012,"Jake"), 
          (2010,"Taylor"), 
          (2008,"Joe"))    
(min_year, max_year, num_people) = get_data(tswift)
print("From", min_year, "to", max_year, \
        "Taylor Swift wrote songs about", num_people, "people!\n")

# Lists
# Lists are ordered sequences of elements
# Lists are mutable - can change the elements
# Tuples and strings are immutable

# Because the lists are mutabel, all the variables that you have pointed will also be changed at the same time becaus eyou change the elements in the memory thos etoherrs are also pointing to

#########################
## EXAMPLE: sum of elements in a list
#########################
def sum_elem_method1(L):
  total = 0 
  for i in range(len(L)): 
      total += L[i] 
  return total
  
def sum_elem_method2(L):
    total = 0 
    for i in L: 
        total += i 
    return total
  
print(sum_elem_method1([1,2,3,4]))
print(sum_elem_method2([1,2,3,4]))


#########################
## EXAMPLE: various list operations
## put print(L) at different locations to see how it gets mutated
#########################
L1 = [2,1,3]
L2 = [4,5,6]
L1.append(4)
L1.extend([0,6])
L3 = L1 + L2
print("L3:", L3, "\n") # I changed here a bit

L = [2,1,3,6,3,7,0]
L.remove(2) # returns None
L.remove(3)
del(L[1])
print("L:", L, "\n") # I changed here a bit
print(L.pop(), "was the last element and removed so L is now:", L, "\n") # returns the last element

s = "I<3 cs"
print(list(s)) # ['I', '<', '3', ' ', 'c', 's'] every character is an element
print(s.split('<')) # ['I', '3 cs'] splits the string by '<' and returns a list of strings
L = ['a', 'b', 'c']
print(''.join(L)) # 'abc' joins the list of strings into a single string
print('_'.join(L)) # 'a_b_c' joins the list of strings into a single string with '_' in between

L=[9,6,0,3]
print(sorted(L)) # [0, 3, 6, 9] returns a new list, does NOT MUTATE L
L.sort() # MUTATES L
L.reverse() # MUTATES L
print()


#########################
## EXAMPLE: aliasing
#########################
a = 1
b = a
print(a)
print(b)

warm = ['red', 'yellow', 'orange']
hot = warm # means that I am creating an alias for this list
# hot and warm both point to the same list/object in memory
hot.append('pink')
print("hot list:", hot)
print("warm list:", warm)

warm = ('red', 'yellow', 'orange')
hot = warm
# hot.append('pink') # error because tuples are immutable
hot += ('pink',) # creates a new tuple and points hot to it
print("hot tuple:", hot)
print("warm tuple:", warm, "\n")

#########################
## EXAMPLE: cloning
#########################
cool = ['blue', 'green', 'grey']
chill = cool[:] # from 0 to len(cool)
chill.append('black')
print("chill:", chill)
print("cool: ", cool, "\n")

#########################
## EXAMPLE: sorting with/without mutation
#########################
warm = ['red', 'yellow', 'orange']
sortedwarm = warm.sort() #mutates warm, but returns None
print("obj.sort\nwarm is sorted now:", warm)
print("sortedwarm:", sortedwarm, "\n")

cool = ['grey', 'green', 'blue']
sortedcool = sorted(cool) # returns a new list, does not mutate cool
print("sorted(obj)\ncool is still the same:", cool)
print("sortedcool is a new list:", sortedcool, "\n")

#########################
## EXAMPLE: lists of lists of lists...
#########################
warm = ['yellow', 'orange']
hot = ['red']
brightcolors = [warm] # list of lists
# a list, element inside the list is a list, which is pointing to that obejct
brightcolors.append(hot) # it just points to a list
print("brightcolors:", brightcolors)
hot.append('pink')
print("hot:", hot)
print("brightcolors:", brightcolors, "\n")


###############################
## EXAMPLE: mutating a list while iterating over it
###############################
def remove_dups(L1, L2):
    for e in L1: # it is going to go to index 1 after removing the first element, however element 2 in index 1 becaome in index 0 and it passes that element
        if e in L2:
            L1.remove(e)
      
def remove_dups_new(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2) # python keeps track of the index and does not update the index
print("after remove_dups L1:", L1, "and L2:", L2, "\n")

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups_new(L1, L2)
print("after NEW remove_dups L1:", L1, "and L2:", L2, "\n")

###############################
## EXERCISE: Test yourself by predicting what the output is and 
##           what gets mutated then check with the Python Tutor
###############################
cool = ['blue', 'green']
warm = ['red', 'yellow', 'orange']
print(cool) # ['blue', 'green']
print(warm) # ['red', 'yellow', 'orange']

colors1 = [cool] # [['blue', 'green']]
print(colors1) # [['blue', 'green']]
colors1.append(warm) # [['blue', 'green'], ['red', 'yellow', 'orange']]
print('colors1 =', colors1) # [['blue', 'green'], ['red', 'yellow', 'orange']]

colors2 = [['blue', 'green'],
          ['red', 'yellow', 'orange']]
print('colors2 =', colors2) # [['blue', 'green'], ['red', 'yellow', 'orange']]

warm.remove('red') # ['yellow', 'orange']
print('colors1 =', colors1) # [['blue', 'green'], ['yellow', 'orange']]
print('colors2 =', colors2) # [['blue', 'green'], ['red', 'yellow', 'orange']]

for e in colors1:
    print('e =', e)
# e = ['blue', 'green']
# e = ['yellow', 'orange']

for e in colors1:
    if type(e) == list:
        for e1 in e:
            print(e1)
    else:
        print(e)
# 'blue'
# 'green'
# 'yellow'
# 'orange'

flat = cool + warm # ['blue', 'green', 'yellow', 'orange']
print('flat =', flat)

print(flat.sort()) # None
print('flat =', flat) # ['blue', 'green', 'orange', 'yellow']

new_flat = sorted(flat, reverse = True) # ['yellow', 'orange', 'green', 'blue']
print('flat =', flat) # ['blue', 'green', 'orange', 'yellow']
print('new_flat =', new_flat) # ['yellow', 'orange', 'green', 'blue']

cool[1] = 'black' # ['blue', 'black']
print(cool) # ['blue', 'black']
print(colors1) # [['blue', 'black'], ['yellow', 'orange']]