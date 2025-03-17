## Un program that we put numbers and it returns the numbers in letters

numero_usuario = input("Enter your phone number: ")

diccionario_numbers = {
     "1": "One", 
     "2" : "Two",
     "3" : "Three", 
     "4" : "Four", 
     "5" : "Five", 
     "6" : "Six", 
     "7" : "Seven", 
     "8" : "Eight", 
     "9" : "Nine", 
}
output_numero_letras = ""

for item in numero_usuario:
    output_numero_letras += diccionario_numbers.get(item, "#") + " "
print(output_numero_letras)
