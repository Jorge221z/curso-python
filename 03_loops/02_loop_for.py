import os
os.system("clear")

#iterar una lista

# frutas = ['manzana', 'pera', 'limon', 'platano']

# for fruta in frutas:
#     print(fruta)

#iterar sobre cualquier cosa iterable

# cadena = "jorge221z"
# for char in cadena:
#     print(char)

#enumerate
frutas = ['manzana', 'pera', 'limon', 'platano']
for index, fruta in enumerate(frutas):
    print(f"El indice {index} tiene {fruta}")


#bucles anidados
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")



animales = ["perro", "gato", "colibri", "elefante", "salmon"]
for i, animal in enumerate(animales):
    if animal == "elefante":
        print(f"El {animal} está en el indice {i}")
        break


#comprensión de listas   (list comprenhension)

animales = ["perro", "gato", "colibri", "elefante", "salmon"]

animales_mayusculas = [animal.upper() for animal in animales]
    
print(animales_mayusculas)

#elementos pares

pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(pares)

