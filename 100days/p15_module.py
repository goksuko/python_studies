logo_art = """
      )  (
     (   ) )
      ) ( (
     _______)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'          
"""


import os

def clear_screen():
    # Clear the screen based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-based systems (Linux, macOS)
        os.system('clear')

data = [
    {
        'name': "espresso",
        'water': 50,
        'coffee': 18,
        'milk': 0,
        'price': 1.50
	},
    {
        'name': "latte",
        'water': 200,
        'coffee': 24,
        'milk': 150,
        'price': 2.50
	},
    {
        'name': "cappucino",
        'water': 250,
        'coffee': 24,
        'milk': 100,
        'price': 3.00
	}
]

coins = [
    {
        'name': "quarters",
		'value': 0.25
	},
	{
		'name': "dimes",
		'value': 0.10
	},
	{
		'name': "nickles",
		'value': 0.05
	},
	{
		'name': "pennies",
		'value': 0.01
	}
]