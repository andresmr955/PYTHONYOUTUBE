import random 

class Dice:
    def __init__(self, name):
        self.name = name
    

    def roll(self):
        for i in range(1):
            total_dice = ()
            first_number = random.randint(1,6)
            total_dice = (*total_dice, first_number) 
            for y in range(1):
                second_number = random.randint(1,6)
                total_dice = (*total_dice, second_number) 
        
            return total_dice

def createUsers():

    dice_one = Dice(input("What is your name?: "))
    print(f'Hello {dice_one.name}, your dice is {dice_one.roll()}')

    dice_two = Dice(input("What is your name?: "))
    print(f'Hello {dice_two.name}, your dice is {dice_two.roll()}')
    