################### Scope ####################

enemies = 1

# def increase_enemies(): # a function that creates a local scope
#   # enemies = 11
#   global enemies # to modify the global variable
#   enemies += 1
#   print(f"enemies inside function: {enemies}")

def increase_enemies_2(enemies): # a function that creates a local scope
  print(f"enemies inside second function: {enemies}")
  return enemies + 1

# increase_enemies()
print(increase_enemies_2(enemies)) # this will not modify the global variable 
print(f"enemies outside function: {enemies}")

# Local scope
print("\nLocal scope")

def drink_potion():
  potion_strength = 2 # defined inside the function, available only inside the function
  print(f"potion_strength inside function: {potion_strength}")

drink_potion()
# potion_strength is not available outside the function
# print(potion_strength)  # NameError: name 'potion_strength' is not defined

# Global scope
print("\nGlobal scope")

player_health = 3 # defined in top of the file, available to all functions

def drink_potion_global():
  potion_strength = 22
  print(f"player_health inside function: {player_health}")
  print(f"potion_strength inside function: {potion_strength}")

drink_potion_global()

# namespaces are valid only in scopes!!
print("\nNamespaces")

def game():
  def drink_potion_inside_game(): #now drink_potion is a local scope
    potion_strength = 222
    print(f"player_health inside game function: {player_health}")
    print(f"potion_strength inside game function: {potion_strength}")
  drink_potion_inside_game()

game()

### ***************************************************************************************** ###
### There is no block scope in Python!!!!
### ***************************************************************************************** ###

print("\nNO_Block scope")

game_level = 3

enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
  new_enemy = enemies[0]

print(new_enemy)  # new_enemy is available outside the if block

# defining new_enemy_inside_function

def create_enemy():
  new_enemy_inside_function = "" ## initialize the variable before using so that if it does not met the requirement, it will not throw an error
  if game_level < 5:
    new_enemy_inside_function = enemies[1]
    print(new_enemy_inside_function)

# print(new_enemy_inside_function) # NameError: name 'new_enemy_inside_function' is not defined

create_enemy()

def is_prime(num):
    answer = True
    n = 2
    while n < num:
        if num % n == 0:
            answer = False
        n += 1

# Global Constants

PI = 3.14159
GOOGLE_URL = "https://www.google.com"

def calc_area(radius):
    return PI * radius ** 2
