from os import system
if system("clear") != 0: system("cls")


# Expresiones regulares

import re

pattern = "Hola"

text = "Hola Mundo"

result = re.search(pattern, text)
print(result.group()) 

# group() devuelve el resultado como si fuese string

# start() devuelve la posicion inicial de la coincidencia

# end() devuelve la posicion final de la coincidencia

#EJERCICIO 1
# Encuentra la primera ocurrencia de la palabra IA en el siguiente texto.
# Devuelve tambien en que posicion empieza y termina la coincidencia

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"
found_ia = re.search(pattern, text)

if found_ia:
  print(f"He encontrado el patrón en el texto en la posición {found_ia.start()} y termina en la posición {found_ia.end()}")
else:
  print("No he encontrado el patrón en el texto")

  # -----------------------

### Encontrar todas las coincidencias de un patrón
# .findall() devuelve una lista con todas las coincidencias

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"

matches = re.findall(pattern, text)

print(len(matches))


# -------------------------

# iter() devuelve un iterador que contiene todos los resultados de la búsqueda

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"

matches = re.finditer(pattern, text)

for match in matches:
  print(match.group(), match.start(), match.end())

print("-------------------------")
# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de Midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"
pattern = "midu"
 
matches = re.finditer(pattern, text, re.IGNORECASE)

for match in matches:
  print(match.group(), match.start(), match.end())


# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"

text = "Hola mundo, Hola de nuevo"

pattern = "Hola"
replacement = "Adiós"

new_text = re.sub(pattern, replacement, text)

print(new_text)