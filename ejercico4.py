#Tabla de multiplicar

#Crea un programa que solicite al usuario un número y muestre la tabla de multiplicar de ese número.

#python

numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")