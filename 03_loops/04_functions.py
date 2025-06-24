import os
os.system("clear")


def saludar():
    print("Hola tigere")

saludar()

print("----------------------------------")

def saludar_a(nombre):
    print(f"Hola {nombre}")

saludar_a("jorge")
saludar_a("midudev")

print("----------------------------------")

def sumar(a, b):
    return a + b

print(sumar(2, 3))

#Docuementar las funciones con docstring

def restar(a, b):
    """Resta dos numeros y devuelve el resultado"""
    return a - b

print(restar.__doc__)

print("----------------------------------")
#parametros por defecto

def multiplicar(a, b = 2):
    return a * b

print(multiplicar(2))  # el segundo parametro es 2 por defecto

print("----------------------------------")
#Argumentos por posicion

def describir_persona(nombre, edad, sexo):
    print(f"Soy {nombre}, tengo {edad}, y me identifico como {sexo}.")

describir_persona("jorge", 25, "gato")

print("----------------------------------")

describir_persona(edad = 21 , sexo = "pez", nombre = "jorge")

print("----------------------------------")
# argumentos de longitud de variable

def suma_numeros(*args):
    suma = 0
    for numero in args:
        suma+= numero
    return suma

print(suma_numeros(1, 2, 3, 4 ,5))


print("----------------------------------")

#arguemntos de clave-valor variable

def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


mostrar_informacion_de(nombre="perico", edad=12, sexo="gato")
print("\n")
mostrar_informacion_de(elmejornombre="perico", edadloca=12, sexoou="gato")