###DRY: DON'T REPEAT YOURSELF

user_option = input("").lower()
while user_option != "quit":
    if user_option == "start":
        print("Car started. Ready to go!")
        user_option = input("").lower()
    elif user_option == "stop":
        print("Car stopped")
        user_option = input("").lower()
    elif user_option == "help":
        print('''
start - to start the car
stop - to stop the car 
quit - to quit
''')
        user_option = input("").lower()
    else:
        print("Sorry, I don't understand")    
        break
print("Finished procces code 0")        