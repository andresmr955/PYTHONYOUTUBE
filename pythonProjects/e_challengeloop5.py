numbers = [5,2,5,2,2]
## you have to use for loop an iterate list's numbers
#for item in numbers:
#    result = "x" * item
#    print(result)

## THAT ONE DOES NOT WORK CAUSE WE NEED A NEESTED LOOP

character = "x"
for item in numbers:
    cajita = ""
    for y in range(item):    
        cajita += character
    print(cajita)     
    
    
        