# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# input

a = float(input("ingrese la longitud del lado 1: "))
b = float(input("ingrese la longitud del lado 2: "))
c = float(input("ingrese la longitud del lado 3: "))

# processing

if a + b > c:
    resultados = "los lados puden formar un triangulo"
    if b + c > a:
        resultado = "los lados pueden formar un triangulo"
        if c + a > b:
            resultados = "los lados pueden formar un triangulo "
        else:
            resultados = "los lados no pueden formar un triangulo "
# output

print("los lados" , a, ",", b, "y", c, resultados)