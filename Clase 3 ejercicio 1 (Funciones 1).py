#Funciones 1

#funcion predefinida "imprimir"

print("Hola clase")
print("Hola clase2")
print("Hola clase3")

print("***********************************************")
#Funcion def()

def mensaje():
    print("Hola clase")
    print("Hola clase2")
    print("Hola clase3")
#Imprimir mensaje
mensaje()

print("***********************************************")
def saludo():
    print ("Saludo")
#Imprime mensaje
saludo()

print("***********************************************")
# las variables de la funcion son solo de la funcion
#toma variables fuera de la definicion, solo sobre la posicion de la llamada de la funcion

def suma():
    numero1 = 5
    numero2 = 6
    print(numero1 + numero2)
#llamado de la funcion
suma()
print("***********************************************")
 #Crear una funcion que recibe parametros o variables

def multiplicacion(num1,num2):
     print("El resultado de la multiplicacion es", num1 * num2)

multiplicacion(1,4)
print("***********************************************")

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: "))

def division (num1, num2):
    if num2 != 0:
        print("El resultado de la multiplicacion es", num1 / num2)
        return num1/num2
    else:
        print("No se puede dividir")
        return "No se puede dividir"
division (num1, num2)
cerar una funcion para calcular el are de un cuadrado rectrangulo y triangulo