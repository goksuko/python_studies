# Creating a string
greeting_string = "Hello, world!"

# Accessing characters using indexing
first_char = greeting_string[0]  # 'H'
last_char = greeting_string[-1]  # '!'

# Making the entire string lowercase
lowercase_greeting = greeting_string.lower()  # 'hello, world!'


# Example string
s = " Hello, World! Welcome to Python. "

# capitalize() - Converts the first character to upper case
print(s.capitalize())  # Output: " hello, world! welcome to python. "

# casefold() - Converts string into lower case
print(s.casefold())  # Output: " hello, world! welcome to python. "

# center() - Returns a centered string
print(s.center(50, '-'))  # Output: "----- Hello, World! Welcome to Python. -----"

# count() - Returns the number of times a specified value occurs in a string
print(s.count("o"))  # Output: 3

# encode() - Returns an encoded version of the string
print(s.encode())  # Output: b' Hello, World! Welcome to Python. '

# endswith() - Returns true if the string ends with the specified value
print(s.endswith("Python."))  # Output: True

# expandtabs() - Sets the tab size of the string
print("Hello\tWorld".expandtabs(4))  # Output: "Hello   World"

# find() - Searches the string for a specified value and returns the position of where it was found
print(s.find("World"))  # Output: 7

# format() - Formats specified values in a string
print("Hello, {}!".format("Python"))  # Output: "Hello, Python!"

# format_map() - Formats specified values in a string (uses a dictionary)
data = {"language": "Python", "year": 2025}
print("I love {language} ({year})".format_map(data))  # Output: "I love Python (2025)"

# index() - Searches the string for a specified value and returns the position of where it was found
try:
    print(s.index("Python"))  # Output: 28
except ValueError:
    print("Not found")

# isalnum() - Returns True if all characters in the string are alphanumeric
print("Python3".isalnum())  # Output: True

# isalpha() - Returns True if all characters in the string are in the alphabet
print("Python".isalpha())  # Output: True

# isascii() - Returns True if all characters in the string are ascii characters
print("Hello".isascii())  # Output: True

# isdecimal() - Returns True if all characters in the string are decimals
print("12345".isdecimal())  # Output: True

# isdigit() - Returns True if all characters in the string are digits
print("12345".isdigit())  # Output: True

# isidentifier() - Returns True if the string is an identifier
print("variable_name".isidentifier())  # Output: True

# islower() - Returns True if all characters in the string are lower case
print(s.islower())  # Output: False

# isnumeric() - Returns True if all characters in the string are numeric
print("12345".isnumeric())  # Output: True

# isprintable() - Returns True if all characters in the string are printable
print("Hello, World!".isprintable())  # Output: True

# isspace() - Returns True if all characters in the string are whitespaces
print("   ".isspace())  # Output: True

# istitle() - Returns True if the string follows the rules of a title
print("Hello World".istitle())  # Output: True

# isupper() - Returns True if all characters in the string are upper case
print("HELLO".isupper())  # Output: True

# join() - Converts the elements of an iterable into a string
print(", ".join(["apple", "banana", "cherry"]))  # Output: "apple, banana, cherry"

# ljust() - Returns a left justified version of the string
print(s.ljust(40, '-'))  # Output: " Hello, World! Welcome to Python. --"

# lower() - Converts a string into lower case
print(s.lower())  # Output: " hello, world! welcome to python. "

# lstrip() - Returns a left trim version of the string
print(s.lstrip())  # Output: "Hello, World! Welcome to Python. "

# maketrans() - Returns a translation table to be used in translations
trans = str.maketrans("aeiou", "12345")
print(s.translate(trans))  # Output: " H5ll4, W4rld! W5lc3m5 t4 Pyth4n. "

# partition() - Returns a tuple where the string is parted into three parts
print(s.partition("World"))  # Output: (' Hello, ', 'World', '! Welcome to Python. ')

# replace() - Returns a string where a specified value is replaced with a specified value
print(s.replace("Python", "Java"))  # Output: " Hello, World! Welcome to Java. "

# rfind() - Searches the string for a specified value and returns the last position of where it was found
print(s.rfind("o"))  # Output: 20

# rindex() - Searches the string for a specified value and returns the last position of where it was found
try:
    print(s.rindex("Python"))  # Output: 28
except ValueError:
    print("Not found")

# rjust() - Returns a right justified version of the string
print(s.rjust(40, '-'))  # Output: "-- Hello, World! Welcome to Python. "

# rpartition() - Returns a tuple where the string is parted into three parts (from right)
print(s.rpartition("World"))  # Output: (' Hello, ', 'World', '! Welcome to Python. ')

# rsplit() - Splits the string at the specified separator, and returns a list
print(s.rsplit(" ", 2))  # Output: [' Hello, World! Welcome', 'to', 'Python. ']

# rstrip() - Returns a right trim version of the string
print(s.rstrip())  # Output: " Hello, World! Welcome to Python"

# split() - Splits the string at the specified separator, and returns a list
print(s.split())  # Output: ['Hello,', 'World!', 'Welcome', 'to', 'Python.']

# splitlines() - Splits the string at line breaks and returns a list
multiline_str = "Hello\nWorld\nPython"
print(multiline_str.splitlines())  # Output: ['Hello', 'World', 'Python']

# startswith() - Returns true if the string starts with the specified value
print(s.startswith(" Hello"))  # Output: True

# strip() - Returns a trimmed version of the string
print(s.strip())  # Output: "Hello, World! Welcome to Python."

# swapcase() - Swaps cases, lower case becomes upper case and vice versa
print(s.swapcase())  # Output: " hELLO, wORLD! wELCOME TO pYTHON. "

# title() - Converts the first character of each word to upper case
print(s.title())  # Output: " Hello, World! Welcome To Python. "

# translate() - Returns a translated string (using maketrans table)
print(s.translate(str.maketrans("aeiou", "12345")))  # Output: " H5ll4, W4rld! W5lc3m5 t4 Pyth4n. "

# upper() - Converts a string into upper case
print(s.upper())  # Output: " HELLO, WORLD! WELCOME TO PYTHON. "

# zfill() - Fills the string with a specified number of 0 values at the beginning
print("42".zfill(5))  # Output: "00042"
