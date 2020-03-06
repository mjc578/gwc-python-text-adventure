# Game file for game variables and methods
import random

#========================
# Game and Utility Data
#========================

dungeonBossesList = ['witch', 'vampyre']
dungeonBossesWeaknesses = {'vampyre' : 'garlic', 'witch' : 'water bucket'}
dungeonBossWeaknessHint = {'vampyre' : 'smelly', 'witch' : 'wet'}
dungeonBoss = random.choice(dungeonBossesList)

weaponChoices = ['dagger', 'sword', 'crossbow', 'axe']
weaponActions = {'dagger' : 'stab', 'sword' : 'slash', 'crossbow' : 'shoot', 'axe' : 'swing'}
specialItemChoices = ['garlic', 'water bucket']

bold_green = "\033[1;32m"
bold_yellow = "\033[1;33m"
red = "\033[31m"
reset_color = "\033[0m"
line_width = 40

#========================
# Game State Variables
#========================

treasureFound = False
leftRoomCleared = False
rightRoomCleared = False
visitedRooms = []

#========================
# Game Methods
#========================

def setCurrentRoom(room):
  currentRoom = room
  visitedRooms.append (room)

def hasVisitedRoom(room):
  try:
    foundIndex = visitedRooms.index(room)
  except ValueError:
    foundIndex = -1

  return foundIndex > -1

def handleInput(prompt, choices):
    print()
    validChoice = False
    while validChoice is False:
        print(prompt)
        print()
        for x in range(0, len(choices)):
            print(f'{x+1} - {choices[x]}')
        print()
        playerInput = input('What do you choose? (Pick the number of your choice)\n')
        print()

        # come back to this ...
        if not playerInput.isnumeric() or int(playerInput) < 1 or int(playerInput) > len(choices):
            print("sorry, that's not one of the choices. \nTry again.")
        else:
            validChoice = True

    return int(playerInput)

def print_room_title(title):
  print (bold_green + "\n\n" + "*" * line_width + reset_color)
  center_print_line (title, "*", bold_green)
  print (bold_green + "*" * line_width + "\n" + reset_color)

def center_print_line( title, decoration, color = reset_color ):
  title_length = len(title)
  if title_length % 2 != 0:
      title = title + " "
      title_length += 1

  if title_length <= 1:
    print (color + decoration * line_width + reset_color)
  elif title_length > line_width - 4:
    print (title)
  else:
    midPoint = int(line_width / 2)
    leftHalfTitle = int(title_length / 2)
    num_stars = midPoint - leftHalfTitle - 1

    print (color + decoration * num_stars + " " + title + " " + decoration * num_stars + reset_color)

def printActionText(line):
    print(red + line + reset_color)
