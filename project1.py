# Mad Libs Python Project

# Input Selection
name = input("Enter your name: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
animal = input("Enter your favorite animal: ")
verb1 = input("Enter a verb ending in -ing: ")
place = input("Enter a magical place: ")
object1 = input("Enter a mystical object: ")
superpower = input("Enter a superpower: ")
emotion = input("Enter an emotion: ")
exclamation = input("Enter an exclamation (e.g. Wow, Yikes): ")

madlib = f"""
Once upon a time, there was a {adjective1} explorer named {name}. With a backpack full of hope and a heart full of dreams, 
{name} set out on a(n) {adjective2} journey riding a loyal {animal}.

While {verb1} through the enchanted forest of {place}, {name} stumbled upon a glowing {object1}. 
As soon as they touched it, they were granted the power of {superpower}!

Suddenly, a voice echoed from the clouds, saying, “{exclamation}! You are the chosen one!”

With bravery in their soul and sparkles in their eyes, {name} soared into the sky, spreading {emotion} 
wherever they went — becoming a legend across the land of {place}.

And from that day forward, the world was never the same again...
"""

print(madlib)