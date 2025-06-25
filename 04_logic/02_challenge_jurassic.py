"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. 
Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y 
devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""


def contar_huevos(array) -> int:
    suma_huevos = 0
    for num in array:
        if num % 2 == 0:
            suma_huevos += num

    return suma_huevos

huevos = [12, 34, 45, 65, 2, 5, 6, 7, 8, 9, 99, 0]

print(f"El total de huevos de dinosaurios carnivoros es: {contar_huevos(huevos)}")