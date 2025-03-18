import random 


class Dice:
    def __init__(self, name):
        self.name = name
    

    def roll(self):
        for i in range(1):
            first_number = random.randint(1,6)
            second_number = random.randint(1,6)

            return first_number, second_number

def createUsers():

    dice_one = Dice("Moush")
    print(f'Hello {dice_one.name}, your dices are {dice_one.roll()}')

createUsers()