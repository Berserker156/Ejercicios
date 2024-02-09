#Factorial de un número

#Escribe un programa que calcule el factorial de un número ingresado por el usuario.

#python

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingresa un número para calcular su factorial: "))
resultado = factorial(numero)
print("El factorial de", numero, "es:", resultado)