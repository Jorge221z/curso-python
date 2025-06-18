###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")


mi_nombre = "John Doe"
mi_ciudad = "New York"
 
print(mi_nombre + "\n" + mi_ciudad)

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
cadena = "12345"

entero = int(cadena)

flotante = float(entero)

print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")
numero = 3.99

print(int(numero))
#se le quitan los decimales

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

mi_nombre = "John Doe"
mi_edad = 21
mi_altura = 1.81

print(f"Me llamo {mi_nombre}, tengo {mi_edad} años y mido {mi_altura}.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

numero_pi = 3.14

numero_pi_redondeado = round(numero_pi)

numero_pi_dividido = numero_pi_redondeado // 2   # Con / se hace la división normal. Con // se hace la división entera, que elimina el resto.

print(numero_pi_dividido)