#Listas
#Conjunto de datos ordenados

lista_numeros = [1,2,3,4,5,6,7,8,9]
print(lista_numeros)
print("*****************************************")
lista_distintos_datos = ["uno", 2, 3.0,"cuatro"]
#imprimir todos los datos
print(lista_distintos_datos)
print("*****************************************")
#inprimir un dato en especifico
print(lista_distintos_datos[0])
print("*****************************************")
#inprimir desde un punto del dato hasta otro
print(lista_distintos_datos[-4:-1])
print("*****************************************")
#Mostrar datos en filas
for datos in lista_distintos_datos:
    print(datos)#mostrar datos de la lista
print("*****************************************")
lista_numeros = [1,2,3,4,5,6,7,8,9]
for numero in lista_numeros:
    print(numero)
print("*****************************************")
#suma de listas (concatenar listas)

lista_uno =[1,2,3,4]
lista_dos =[5,6,7,8]

print("Suma de listas: ",lista_uno+lista_dos)
print("*****************************************")
lista_uno =[1,2,3,4]
lista_dos =[5,6,7,8]
lista_tres = lista_uno+lista_dos
#reemplazar datos(MUTABILIDAD)
lista_tres[4]=9
print(lista_tres)
#append(Añadir dato a lista)
lista_tres.append(5)
print(lista_tres)
#insertar dato en lista
lista_tres.insert(0,0)
print(lista_tres)
#eliminar dato de lista
lista_tres.remove(9)
print(lista_tres)
#imprimir longitud de lista
print(len(lista_tres))
print("*****************************************")
#Sobreescribir lista hasta punto 5
lista_tres[:5] = ["a","b","b","d","e"]
print(lista_tres)