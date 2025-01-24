print("Hello World!")

# Import the random library to use for the dice later
import random

# Coding Question 1
diceOptions = list(range(1, 7)) # 1 - 6, 7 is excluded

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"] 

# Coding Question 2
print("Available weapons: ")
for weapon in weapons:
    print(f"- {weapon}")

# Coding Question 3
combatStrength = int(input("Enter your combat Strength: (Number between 1-6) "))
if (combatStrength < 1 or combatStrength > 6):
    print("Input must be an integer between 1-6")
else :
    mCombatStrength = int(input("Enter the monster's combat Strength: "))
    if (mCombatStrength < 1 or mCombatStrength > 6):
        print("Input must be an integer between 1-6")
    
# Coding Question 4
for i in range(1, 21, 2):
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    heroTotal = heroRoll + combatStrength
    monsterTotal = monsterRoll + mCombatStrength

    print(f"Round {i}:\n Hero rolled {heroRoll} with {heroWeapon} and total of {heroTotal}\n Monster rolled {monsterRoll} with {monsterWeapon} and total of {monsterTotal}")
    if heroTotal > monsterTotal:
        print("Hero wins")
    elif heroTotal < monsterTotal:
        print("Monster wins")
    else:
        print("Tie")
    
    if i == 11:
        print(f"\n Battle Truce!")
        break