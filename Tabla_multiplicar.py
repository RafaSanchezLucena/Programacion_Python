# Descripción: Este programa muestra la tabla de multiplicar de un número dado
# Versión: 1.0
# Autor: Rafael Sánchez
# Fecha: 20/01/2021


print("## TABLA DE MULTIPLICAR ##")

# Preguntamos por un número para calcular la tabla 

numero = int(input("Dame un número: "))
print(" ")

# Cálculo del resultado

for i in range (1, 11):
    print(numero, "x", i, "=", numero * i)
print(" ")
print("Fin del programa")

