# ========== PYTHON EQUALITY RULES SUMMARY ==========

# Order Matters:
# - Lists [] - Position matters
# - Tuples () - Position matters  
# - Strings "" - Character order matters

# Order Doesn't Matter:
# - Sets {} - Only unique elements matter
# - Dictionaries {} - Key-value pairs, order irrelevant (Python 3.7+)
# - Frozensets - Immutable sets, order irrelevant

# Key Points:
# - Type matters: [1,2,3] != (1,2,3) (list vs tuple)
# - Case sensitive: "abc" != "ABC"
# - Nested structures: Follow rules of their container and contents
# - Special cases: True == 1 and False == 0 in Python
# - Empty collections: All empty collections of same type are equal

# ========== SET EQUALITY (Order doesn't matter) ==========
set([1, 2, 3]) == set([3, 1, 2])  # True
set([1, 2, 3]) == set([2, 3, 1])  # True
set("abc") == set("bca")          # True
set("abc") == set("cab")          # True

# These are not equal (different elements):
set([1, 2, 3]) == set([1, 2, 4])  # False
set("abc") == set("abd")          # False

# ========== LIST EQUALITY (Order DOES matter) ==========
[1, 2, 3] == [1, 2, 3]  # True
[1, 2, 3] == [3, 1, 2]  # False - different order
[1, 2, 3] == [1, 2, 3, 1]  # False - different length
["a", "b"] == ["a", "b"]  # True
["a", "b"] == ["b", "a"]  # False - different order

# ========== TUPLE EQUALITY (Order DOES matter) ==========
(1, 2, 3) == (1, 2, 3)  # True
(1, 2, 3) == (3, 1, 2)  # False - different order
(1, 2, 3) == (1, 2, 3, 1)  # False - different length
("a", "b") == ("a", "b")  # True
("a", "b") == ("b", "a")  # False - different order

# ========== DICTIONARY EQUALITY (Order doesn't matter in Python 3.7+) ==========
{"a": 1, "b": 2} == {"b": 2, "a": 1}  # True - same key-value pairs
{"a": 1, "b": 2} == {"a": 1, "b": 3}  # False - different values
{"a": 1, "b": 2} == {"a": 1}  # False - different keys

# ========== STRING EQUALITY (Order DOES matter) ==========
"abc" == "abc"  # True
"abc" == "bca"  # False - different order
"abc" == "ABC"  # False - case sensitive
"hello" == "hello"  # True

# ========== FROZENSET EQUALITY (Order doesn't matter) ==========
frozenset([1, 2, 3]) == frozenset([3, 1, 2])  # True
frozenset("abc") == frozenset("bca")  # True
frozenset([1, 2]) == frozenset([1, 2, 3])  # False - different elements

# ========== COMPLEX NESTED STRUCTURES ==========
# Lists containing sets (order of list matters, order within sets doesn't)
[{1, 2}, {3, 4}] == [{1, 2}, {3, 4}]  # True
[{1, 2}, {3, 4}] == [{2, 1}, {4, 3}]  # True - sets are equal
[{1, 2}, {3, 4}] == [{3, 4}, {1, 2}]  # False - list order matters

# Sets containing tuples (tuples must be exactly the same)
{(1, 2), (3, 4)} == {(3, 4), (1, 2)}  # True - set order doesn't matter
{(1, 2), (3, 4)} == {(2, 1), (4, 3)}  # False - tuple order matters

# ========== SPECIAL CASES ==========
# Empty collections
[] == []  # True
{} == {}  # True
set() == set()  # True
() == ()  # True

# Different types
[1, 2, 3] == (1, 2, 3)  # False - list vs tuple
{1, 2, 3} == [1, 2, 3]  # False - set vs list
"123" == 123  # False - string vs int

# None and boolean
None == None  # True
True == True  # True
False == False  # True
True == 1  # True (special case in Python)
False == 0  # True (special case in Python)