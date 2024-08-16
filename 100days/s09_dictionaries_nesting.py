# {"key": "value"}

programming_dictionary = {
	"Bug": "An error in a program that prevents the program from running as expected.", 
	"Function": "A piece of code that you can easily call over and over again.",
	"Loop": "The action of doing something over and over again.",
	123: "Number"}

# Retrieving items from dictionary.
print(programming_dictionary["Bug"])
print(programming_dictionary[123])

# Adding new items to dictionary.
programming_dictionary["While"] = "A loop that continues to run as long as the condition is True."
print(programming_dictionary)

# Create an empty dictionary.
empty_dictionary = {}

# Wipe an existing dictionary.
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary.
programming_dictionary = {
	"Bug": "An error in a program that prevents the program from running as expected.", 
	"Function": "A piece of code that you can easily call over and over again.",
	"Loop": "The action of doing something over and over again."}
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary.
for key in programming_dictionary:
	print(key) #just gives the keys
	print(programming_dictionary[key]) #gives the values

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for key in student_scores:
  if student_scores[key] >= 91:
    student_grades[key] = "Outstanding"
  elif student_scores[key] >= 81:
    student_grades[key] = "Exceeds Expectations"
  elif student_scores[key] >= 71:
    student_grades[key] = "Acceptable"
  else:
    student_grades[key] = "Fail"

# for student in student_scores:
#   score = student_scores[student]
#   if score > 90:
#     student_grades[student] = "Outstanding"
#   elif score > 80:
#     student_grades[student] = "Exceeds Expectations"
#   elif score > 70:
#     student_grades[student] = "Acceptable"
#   else:
#     student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

# Nesting
capitals = {
	"France": "Paris",
	"Germany": "Berlin"
}

# Nesting a List in a Dictionary
travel_log = {
	"France": ["Paris", "Lille", "Dijon"],
	"Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting Dictionary in a Dictionary
travel_log = {
	"France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
	"Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

# Nesting Dictionary in a List
travel_log = [
	{
		"country": "France", 
		"cities_visited": ["Paris", "Lille", "Dijon"], 
		"total_visits": 12
	},
	{
		"country": "Germany",
		"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
		"total_visits": 5
	}
]

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 

def add_new_country(name_country, times, list_of_cities):
  travel_log.append({"country": name_country,
    "visits": times,
    "cities": list_of_cities})

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

