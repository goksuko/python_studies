logo_art = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ /_/_/\__, /_/ /_/\___/_/     
 _   ___/____/                   
| | / / ___/                     
| |/ (__  )                      
|___/____/                       
   / /   ____ _      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/                       

"""

vs_logo = """         
 _   _______
| | / / ___/
| |/ (__  ) 
|___/____/  
            
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
        'name': 'Katy Perry',
        'follower_count': 109,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 250,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 20,
        'description': 'Actor',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 2500,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 50,
        'description': 'Reality TV personality',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 240,
        'description': 'Footballer',
        'country': 'Argentina'
    }
]