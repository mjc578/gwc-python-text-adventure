import time
from player import *
from game import *
from art import *

def centerRoom(player):
    prompt = 'You can enter either the left or right door.'
    choices = ['Enter the left door.', 'Enter the right door.']
    thisRoom = 1

    print_room_title('Starting Room')

    if hasVisitedRoom(thisRoom) == False:
        print('You have journeyed deep into the dungeon and find yourself in a room with three doors.')
        print('There are two doors to the left and to the right and a large door straight ahead.')
        print('Upon further inspection, the large door is locked and the two smaller doors are unlocked.')

    if leftRoomCleared == True and rightRoomCleared == True:
        prompt = 'In addition to the left and right doors, the large center door has opened! You may now go through it.'
        choices.append('Enter the center door.')

    setCurrentRoom(thisRoom)
    actionPicked = handleInput(prompt, choices)

    if actionPicked == 1:
        leftRoom(player)
    elif actionPicked == 2:
        rightRoom(player)
    else:
        bossRoom(player)

def leftRoom(player):
    global leftRoomCleared
    device = 'lever'
    action = 'pull'
    prompt = 'There is nothing left to do in here. You can exit the room.'
    choices = ['Exit the room.']
    thisRoom = 2

    print_room_title('Left Room')

    if hasVisitedRoom(thisRoom) == False:
        print(f'In this room, you notice a {device} on the wall.')
        print(f'You deduce that {action}ing it might do someting.')

    if leftRoomCleared == False:
        choices.append(f'{action} the {device}')
        prompt = f'You can either exit the room or {action} the {device}.'

    setCurrentRoom(thisRoom)
    actionPicked = handleInput(prompt, choices)

    if actionPicked == 1:
        printActionText('You exit the room.')

    if actionPicked == 2:
        printActionText(f'You {action} the {device}. Seeing nothing else to do here, you exit the room.')
        leftRoomCleared = True

    centerRoom(player)

def rightRoom(player):
    global rightRoomCleared
    prompt = 'There is nothing left to do in here. You can exit the room.'
    choices = ['Exit the room.']
    thisRoom = 3

    print_room_title('Right room')

    if hasVisitedRoom(thisRoom) == False:
        print('In this room, you find nothing but an empty room!')
        print('You look around but find nothing of worth anywhere!')
        print('You go to leave the room feeling slightly disappointed...')
        time.sleep(8)
        print('But suddenly behind you...')
        time.sleep(3)
        print('You hear something...')
        time.sleep(3)

    if rightRoomCleared == False:
        prompt = 'You can attack it with your weapon, shine your lantern at it, or flee in terror.'
        choices = ['Attack with weapon.', 'Shine your lantern.', 'Flee in terror!']
        print(boo)
        print(ghost1)
        print('Agh! A ghost!')

    setCurrentRoom(thisRoom)
    actionPicked = handleInput(prompt, choices)

    if rightRoomCleared == False:
        while actionPicked == 1:
            printActionText(f'You {weaponActions[player.playerWeapon]} at the ghost with your {player.playerWeapon}.')
            printActionText(f'Your attack goes right through the ghost!')
            printActionText('You can see the ghost is visibly entertained by your futile attempt to hurt it.')
            actionPicked = handleInput(prompt, choices)

        if actionPicked == 2:
            rightRoomCleared = True
            printActionText('The light banishes the ghost away! Seeing nothing else here, you exit the room.')

        elif actionPicked == 3:
            printActionText('You high-tail it out of there! You didn\'t even know you could run this fast!')
            printActionText('You hear the ghost chuckle at your scaredy-cat tendencies. You feel somewhat... embarassed.')
    else:
        printActionText('You exit the room')

    centerRoom(player)


def bossRoom(player):
    printActionText('This is DLC nerd! Pay up!!')

def initializePlayer():

    playerName = input('Every adventurer needs a name. What is your name?\n')
    playerTown = input('What town/city does your adventurer come from?\n')

    pInput = handleInput("You can choose whatever weapon you want to brave the dungeon.", weaponChoices)
    playerWeapon = weaponChoices[pInput - 1]

    print(f'Someone in town told you that the boss in the dungeon might be weak to something {dungeonBossWeaknessHint[dungeonBoss]}.')
    pInput = handleInput('That said, choose a special item to bring into the dungeon.', specialItemChoices)
    playerSpecialItem = specialItemChoices[pInput - 1]

    return Player(playerName, playerTown, playerWeapon, playerSpecialItem)

def main():
    center_print_line('Welcome to the game!', '*')
    player = initializePlayer()
    player.printGameStartMessage()
    input(red + 'Press enter to begin the game' + reset_color)
    centerRoom(player)

if __name__ == '__main__':
    main()
