#========================
# Player Class
#========================

class Player:

    def __init__(self, name, town, playerWeapon, specialItem):
        self.name = name
        self.town = town
        self.playerWeapon = playerWeapon
        self.specialItem = specialItem

    def printGameStartMessage(self):
        print('*======================================================================*')
        print(f'And so {self.name}, you journey from your town of {self.town} with your')
        print(f'{self.playerWeapon} and {self.specialItem} in hand. Good luck!')
        print('*======================================================================*')
