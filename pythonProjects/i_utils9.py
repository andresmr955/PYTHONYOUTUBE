def find_max(lista):
    max = lista[0]

    for number in lista:
        if number > max:
            max = number
    return max