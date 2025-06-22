###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

n1 = input("Introduce el primer numero\n")
n2 = input("Introduce el segundo numero\n")

if (n1 > n2):
    print(n1 + " es mayor que " + n2)
elif (n1 < n2):
    print(n2 + " es mayor que " + n1)
elif (n1 == n2):
    print("Los numeros son iguales")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

n1 = int(input("Introduce el primer numero\n"))
n2 = int(input("Introduce el segundo numero\n"))

operacion = input("Que quieres hacer? (+, -, * , /)")

if (operacion == "+"):
    print(n1+n2)
elif (operacion == "-"):
    print(n1-n2)
elif (operacion == "*"):
    print(n1*n2)
elif (operacion == "/" and n2 != 0):
    print(n1 / n2)
elif (operacion == "/" and n2 != 0):
    print("La división entre 0 no se permite")
else: 
    print("Operación no especificada")

    
# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

año = int(input("Introduce un año para determinar si es bisiesto\n"))

if (año % 4 == 0 and not (año % 100 == 0 and año % 400 != 0)):
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} no es bisiesto")




# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("Introduce una edad para clasificarla\n"))

if(edad < 0):
    print("Edad no contemplada")
elif (edad >= 0 and edad <= 2):
    print("Eres un bebé!")
elif (edad <= 12):
    print("Eres un niño!")
elif (edad <= 17):
    print("Eres un adolescente")
elif (edad <= 64):
    print("Eres adulto!")
else:
    print("Estas mayorcico")
