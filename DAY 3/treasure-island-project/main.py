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

direction = input("Choose the direction you want to go in.. Left or Right?: ")
chosen_one = ("left")

if direction.lower() == chosen_one:
  print("You may proceed further")
else:
  print("You fell into a pit! GAME OVER")
  exit()
next_action = input("Make your next move.. Swim or Wait?: ")
action_chosen = ("wait")

if next_action.lower() == action_chosen:
  print("You've reached the hall of doors..")
else:
  print("Attacked by trout! GAME OVER!!")
  exit()
doors = input("It's make it or break it!! Which door would you choose? Red, Blue or Yellow?: ")
door_one = ("yellow")
door_two = ("red")
door_three = ("blue")

if doors.lower() == door_one:
  print("You Win!!")

elif doors.lower() == door_two:
  print("Burned by fire! GAME OVER!!")

elif doors.lower() == door_three:
  print("Eaten by Beasts! GAME OVER!!")
else:
  print("GAME OVER!")