 #Contador de vocales

#Escribe un programa que cuente el número de vocales en una cadena de texto ingresada por el usuario.

#python

cadena = input("Ingresa una cadena de texto: ")
vocales = "aeiouAEIOU"
contador_vocales = 0

for letra in cadena:
    if letra in vocales:
        contador_vocales += 1

print("Número de vocales en la cadena:", contador_vocales)