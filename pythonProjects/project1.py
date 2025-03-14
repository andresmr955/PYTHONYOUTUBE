##PROJECT:Weight converter
input("This project is to convert your weight from pounds to kilos, so please press any key to continue")
weightCustomer = float(input('What is your weight in pounds? '))
weightCustomerKilos = weightCustomer * 0.45
print(f'Your weight in Kilos is {weightCustomerKilos}')

##PROJECT WITH MORE DETAILS AND IF CONDITIONALS
pounds_in_kilos = 0.4536
customerWeightNumbers = float(input("What is your weight in numbers?"))
customerWeightMeasure = input("Plase chose the measure of your weight, (L)lbs or (K)Kilos: ")
if type(customerWeightNumbers) == float and customerWeightMeasure == "L":
    customerWeightKilosX = customerWeightNumbers * pounds_in_kilos
    print(f'Your weight in Kilos is {customerWeightKilosX}')
elif type(customerWeightNumbers) == float and customerWeightMeasure == "K":
    customerWeightPounds = customerWeightNumbers / pounds_in_kilos
    print(f'Your weight in pounds is {customerWeightPounds}')
else:
    print(f'Please enter a valid number and measure')