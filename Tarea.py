#crear una funcion para calcular el area de un cuadrado rectrangulo y triangulo
print("Para elegir figura seleccione 1 : Cuadrado / 2 : Triangulo / 3 : Rectangulo")
figura = int(input("seleccione una figura:"))
if figura == 1:
    lado = int(input("ingrese lado del cuadrado (CM) :"))
    def area():
        return lado ** 2
    print("el area del cuadrado es:", area())
if figura == 2:
    base = int(input("ingrese  base del triangulo (CM) :"))
    altura = int(input("ingrese  altura del triangulo (CM) :"))
    def area():
        return (base * altura) / 2
    print("el area del triangulo es:", area())
if figura == 3:
    base = int(input("ingrese  base del rectangulo (CM) :"))
    altura = int(input("ingrese  altura del rectangulo (CM) :"))
    def area():
        return (base * altura) ** 2
    print("el area del rectangulo es:", area())
