

num1=int(input("ingrese numero: "))
num2=int(input("ingrese numero: "))
def comparacion(num1,num2):
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    if num1 == num2:
        return 0

resultado = comparacion(num1,num2)
print(resultado)
print(comparacion(num1,num2))
