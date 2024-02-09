# Calcular el promedio de calificaciones de un grupo de estudiantes
cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

calificaciones = []
for i in range(cantidad_estudiantes):
    calificacion = float(input(f"Ingrese la calificación del estudiante {i+1}: "))
    calificaciones.append(calificacion)

promedio = sum(calificaciones) / cantidad_estudiantes
print(f"El promedio de calificaciones del grupo es: {promedio}")
