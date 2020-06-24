#OPERADORES DE COMPARACION
#if:else:elif

numero1 = int(input('Ingrese número 1: '))
numero2 = int(input('Ingrese número 2: '))

if numero1 == numero2:
    print('los números son iguales')
elif numero1 > numero2:
    print('El número mayor es: ', numero1)
else:
    print('El número mayor es: ', numero2)

#OR

if numero1 == numero2:
    print('los numeros son iguales')
else:
    if numero1 > numero2:
        print('El número mayor es: ', numero1)
    else:
        print('El número mayor es: ', numero2)
