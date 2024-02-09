#En Python, el concepto de "punteros" no se maneja de la misma manera que en lenguajes de programación
# de más bajo nivel como C o C++. Sin embargo, Python maneja referencias a objetos. Las variables en Python 
#almacenan referencias a objetos en lugar de los propios objetos. Aunque no hay punteros explícitos en Python 
#como en otros lenguajes, se pueden simular utilizando referencias a objetos. Aquí tienes un ejemplo que ilustra 
#cómo las referencias a objetos funcionan de manera similar a los punteros:

#python

# Definimos una función para modificar un valor a través de una referencia
def modificar_valor(ref):
    ref[0] = 10

# Creamos una lista y la pasamos a la función como referencia
lista = [1, 2, 3]
print("Antes de modificar:", lista)

modificar_valor(lista)
print("Después de modificar:", lista)