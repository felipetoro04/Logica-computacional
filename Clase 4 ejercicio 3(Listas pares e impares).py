
lista_pares = []
lista_impares = []
contador = 0

for i in range(1,11):
    if (i % 2 == 0):
        lista_pares.append(i)
        contador = contador + 1

    else:
        lista_impares.append(i)
print("Numero pares: ",lista_pares)
print("Numero impares: ",lista_impares)






