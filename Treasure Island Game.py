#This is the code of project 3 of Day 3. To know more about the functioning of this code, please visit - https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
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
direction_1 = input("Where would you like to go ?, left or right ? \n")
if (direction_1 == "left") or (direction_1 == "Left") or (direction_1 == "LEFT"):
  s_or_w = input("Welcome to stage 2. Would you prefer to swim or wait ? \n")
  if s_or_w == "wait" or s_or_w == "Wait" or s_or_w == "WAIT":
    door = input("Welcome to stage 3. You see a door. Which door would you prefer?, Select color among red, yellow, blue or any other color ? \n")
    if door == "red":
      print ("Burned by Fire. Game Over.")
    elif door == "blue":
      print ("Eaten by beasts. Game over.")
    elif door == "yellow":
      print ("You Win !")
    else:
      print ("Game Over")
  else:
    print ("Attacked by trout. Game Over")
else:
  print ("Fell into a hole. Game over")
