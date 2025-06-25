from os import system
if system("clear") != 0: system("cls")

import re

# *  coincide con cero o mas ocurrencias del caracter anterior
text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches)  # ['aaa', '', 'b', ''] - incluye coincidencias vacías

#Ejercicio 1: ¿Cuantas palabras tienen de 0 a más 'a' y después una b?
text = "aaaba aab ab aa b"
pattern = "a"
matches = re.findall(pattern + "*b", text)
print(f"Hay {len(matches)} palabras que tienen de 0 a más 'a' y después una 'b': {matches}")

# cero o una vez

text = "aaabacb"

pattern = r"a?b"
matches = re.findall(pattern, text)
print(matches)  # ['ab', 'cb'] - incluye coincidencias vacías


