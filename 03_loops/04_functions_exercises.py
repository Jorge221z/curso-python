# Vamos a rehacer algunos ejercicios anteriores pero usando funciones
import os
os.system("clear")
# Ejercicio 1: Tabla de multiplicar
# Se le pasa un numero como parametro.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
# print("\nEjercicio 5:")

def tabla_multiplicar(num):
    for n in range(0, 11):
        print(num * n)

tabla_multiplicar(8)


print("----------------------------------")
# Ejercicio 2: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".

def validar_contraseña(pwd):
    while len(pwd) < 8:
        pwd = input("Introduce una contraseña de al menos 8 caracteres")
    print("La contraseña es segura")


pwd = input("Introduce una contraseña\n")
validar_contraseña(pwd)


print("----------------------------------")
# Ejercicio 3: Buscar el máximo de una lista

def buscar_max(lista):
    max = lista[0]
    for num in lista:
        if num > max:
            max = num
    print(f"El maximo es: {max}")

numeros = []
while True:
    num = input("Introduce un numero(Pulsa enter para salir)\n")
    if num == "":
        break
    numeros.append(int(num))

buscar_max(numeros)

print("----------------------------------")
# Ejercicio 4: Imprimir números pares



def imprimir_pares(lista):
    for num in lista:
        if (num % 2 == 0):
            print(num)


lista = [2, 5, 76, 9, 2, 6, 123, 454]
imprimir_pares(lista)