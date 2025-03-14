input('''
Welcome to the number guessing name!
    I am Andres the creator and We will use loops, variabels, and conditions
    You just have to try to guess the number.
    You will have 3 opportunities to guess
    Good luck! The Game starts now!
    Press Enter to continue''')
userNumber = int(input("Enter the number: "))
guess_limit = 3
cont = 1
secret_number = 9
while cont <= guess_limit:
    if userNumber == secret_number:
        print(f'Congratulations!, you guessed the number {userNumber}')
        break
    elif userNumber != secret_number:
        if(cont == guess_limit):
            print(f'You have lost {cont} opportunities, GAME OVER!')
            #break is going to stop the loop
            break
        print(f'You have lost {cont} opportunities left')
        cont += 1
        userNumber = int(input("Enter the number: "))
        
