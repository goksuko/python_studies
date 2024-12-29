
# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.

x = 1 # to be deleted

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The 'try except' is finished")
  
print("")

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
  
# print("")

# x = -1

# if x < 0:
#   raise Exception("Sorry, this number is below zero")

# print("")

# x = "hello"

# if not type(x) is int:
#   raise TypeError("Only integers are allowed")

print("")

x = "Hello"
# x += 1

try:
  	x += 1
except TypeError:
    print("Type error")
except:
    print("Unknown error")
else:
    print("No error")
    print(x)