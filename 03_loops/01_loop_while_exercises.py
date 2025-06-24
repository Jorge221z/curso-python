import os
os.system("clear")

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

# contador = 10

# while contador > 0:
#     print(contador)
#     contador -= 1   #importante poner -= en lugar de =-

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

# suma_pares = 0
# num = 1

# while num <= 20:
#     if num % 2 == 0:
#         suma_pares += num
#     num += 1
# else:
#     print(suma_pares)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

# num = int(input("Introduce un numero para calcular su factorial\n"))
# contador = num
# factorial = 1

# while contador >= 1:
#     factorial *= contador
#     contador= contador - 1 
# else:
#     print(f"Resultado: {factorial}")


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

# pwd = input("Write your password")

# while len(pwd) < 8:
#         pwd = input("Password must have be at least 8 characters")
# else:
#     print("Valid password!")


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
# print("\nEjercicio 5:")

# num = int(input("Write a number between 1 and 10\n"))
# contador = 1
# print(f"Tabla del {num}")
# while contador <= 10:
#     print(num*contador)
#     contador += 1    

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

num = int(input("Introduce un entero positivo\n"))
i = 2
j = 2
es_primo = True

while i <= num:
    j = 2
    es_primo = True
    while (j <= (i-1)):
        if (i % j == 0):
            es_primo = False
            break
        j += 1
    if es_primo == True:
            print(f"El {i} es primo")
    i += 1