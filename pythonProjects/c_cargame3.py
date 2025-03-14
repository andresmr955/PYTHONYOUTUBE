###DRY: DON'T REPEAT YOURSELF
car_on = False
user_option = ""
while True:
    user_option = input("").lower()
    if user_option == "start":
        if user_option == "start" and car_on == True:
            print("Car is already started")
        elif user_option == "start":
            car_on = True
            print("Car started. Ready to go!")
    elif user_option == "stop":
        if user_option == "stop" and car_on == False:
            print("Car is already stopped")
        elif user_option == "stop":
            car_on = False
            print("Car stopped!")
    elif user_option == "help":
        print('''
start - to start the car
stop - to stop the car 
quit - to quit
''')
    elif user_option == "quit":
        print("Finished process code 0")   
        break       
    else:
        print("Sorry, I don't understand")  
 