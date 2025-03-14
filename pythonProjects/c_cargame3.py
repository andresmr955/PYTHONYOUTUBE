###DRY: DON'T REPEAT YOURSELF
car_on = False
user_option = ""
while True:
    user_option = input("").lower()
    if user_option == "start":
        if car_on:
            print("Car is already started")
        else:
            car_on = True
            print("Car started. Ready to go!")
    elif user_option == "stop":
        if not car_on:
            print("Car is already stopped")
        else:
            car_on = False
            print("Car is stopped")

       # if car_on:
       #    car_on = False 
       #    print('Car is stopped')
       # else: 
       #    print("Car is already stopped")
       #         
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
 