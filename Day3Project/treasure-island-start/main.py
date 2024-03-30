print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
choice1 = input("Leaving the beach, you come to a fork in the road. Do you go left or right? ").lower()
if choice1 == "left":
    choice2 = input("You come to a river. Do you swim or wait? ").lower()
    if choice2 == "wait":
        choice3 = input("You come to a house with three doors. Which do you choose? Red, yellow, or blue? ").lower()
        if choice3 == "yellow":
            print("You win!")
        elif choice3 == "red":
            print("You are burned by fire. Game over.")
        elif choice3 == "blue":
            print("You are eaten by beasts. Game over.")
        else:
            print("Game over.")
    else:
        print("You are attacked by a trout. Game over.")
else:
    print("You fall into a hole. Game over.")
