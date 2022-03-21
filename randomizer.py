"""
--- 11 March 2022 ---
This is a python script used to randomize powers. 
Paste the code to the below website and run it. 
In the event a duplicate is rolled, the script will automatically reroll and output a valid set. 
If you do not have all powers unlocked, just delete the powers you do not have and you should be all set. 
Good luck and have fun :D
https://replit.com/languages/python3
"""

import random
Powers = ("Homing", "Jump", "Brake", "Thick", "One Shot", "Mine", "Zap", "Low-res", "Thin", "Scatter Shot", "Steer-less", "Speed Burst", "Stealth Mine", "Trippy", "Power Dash", "Side Shot", "Speedy", "Shield", "Clock Block", "Time Bomb", "Hide Self", "Curve-blind", "Angle Turns", "Multi Shot", "Trigger Bomb", "180", "Double Shot", "Reverse", "Laser", "Teleport")
def roll():
    a = random.choice(Powers)
    b = random.choice(Powers)
    if a == b:
        print(a, "&", b,": Duplicate found, rerolling...")
        roll()
    else:
        print("Power 1:", a, "\nPower 2:", b, "\nGood luck and have fun :D", sep='\n')

roll()