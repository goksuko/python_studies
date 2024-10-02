def my_function():
	result = 3 * 2
	return result

output = my_function()
print(output) # 6

def format_name(f_name, l_name):
	"""Take a first and last name and format it to return the title case version of the name.""" # docstring: explanation of the function
	formatted_f_name = f_name.title()
	formatted_l_name = l_name.title()
	return f"{formatted_f_name} {formatted_l_name}"

output = format_name("anGela", "yu")
print(output) # Angela Yu

def is_leap(year):
  """Take a year and return if it's a leap year."""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) == True and month == 2:
    return 29
  else:
    return month_days[month - 1]

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: ")) # Enter a year
month = int(input("Enter a month: ")) # Enter a month
days = days_in_month(year, month)
print(days)

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25)) # None