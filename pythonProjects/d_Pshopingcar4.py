##Calculate the total cost of all items in a shopping cart
prices = [10, 20,30]
#using for loop
totalCost = 0
for item in prices:
    totalCost += item
print(f'The total cost of the shooping cart is => {totalCost}')