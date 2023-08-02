print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

step_one = input("You're at a crossroad, where do you go? Type 'left' or 'right'? \n").lower()

if step_one == "left":
    step_two = input("You see a lake, there is an island in the middle, a boat is approaching you. Type 'wait' or 'swim'? \n").lower()
    if step_two == "wait":
        step_three = input("The boat takes you to the island. There are 3 doors, 'yellow', 'blue' and 'red', which colour do you choose? \n").lower()
        if step_three == "yellow":
            print("You enter the yellow door, it is filled with gold as bright as the sun. You Win!")
        elif step_three == "blue":
            print("You enter the blue door, the room suddenly fills with water. You lose!")
        elif step_three == "red":
            print("You enter the red room, suddenly eveeything is on fire. You Lose!")
        else:
            print("Invalid Answer! Try again!")
    elif step_two == "swim":
        print("As you are swimming, suddenly something pulls you into the water, its a kraken! You lose!")
    else:
        print("Invalid Answer! Try again!")
elif step_one == "right":
    print("You fall into a hole filled with snakes! Game Over!")
else:
    print("Invalid Answer! Try again!")


