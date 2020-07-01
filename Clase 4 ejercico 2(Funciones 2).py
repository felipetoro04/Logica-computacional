def funcionFor():
    print("funcion for")
    for num in lista1:
        print("nummero:",num)
        print(f"dentro de for {num}")

#creamos lista
lista1 =[1,8,9,8,5]

#llamdo funcion
funcionFor()
print("*****************************************")
#rango de 0 a 6
for num in range(6):
    print(f"numero en rango {num}")
print("*****************************************")
# rango de 1 a 5
for num in range(1,6):
    print(f"numero en rango {num}")
print("*****************************************")
lista = []
var1= int(input("Tamaño de lista: "))
contador = 0
for x in range(var1):
    contador = contador +1
    print("contador:",contador," variable :",x)
    lista.append(x)
print(len(lista))
print(lista)


