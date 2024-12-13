# 6 Dictionaries

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	# 'total': 5,
	}

print("Jen's favorite language is " + favorite_languages['jen'] + ".")
print("Jen's favorite language is " + favorite_languages['jen'].title() + ".")
# print("Total number of languages: " + str(favorite_languages['total']) + ".")
# print("Total number of languages: " + favorite_languages['total'] + ".") # does not work

for key, value in favorite_languages.items():
	print(key.title() + "'s favorite language is " + value.title() + ".")
    


for key in favorite_languages: # same as for key in favorite_languages.keys():
# for key in favorite_languages.keys(): # Looping through the keys is actually the default behavior
	print(key.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
 		print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")
   
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")
 
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())
 
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())
 
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)
 
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}

print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping)

users = {
	'aeinstein': {
	'first': 'albert',
	'last': 'einstein',
	'location': 'princeton',
	},
	'mcurie': {
	'first': 'marie',
	'last': 'curie',
	'location': 'paris',
	},
	}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())