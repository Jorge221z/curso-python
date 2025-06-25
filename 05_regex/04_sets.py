from os import system
if system("clear") != 0: system("cls")


import re

username = "rubius_4$3-_"

pattern = r"[\w._%+-]+"

matcht = re.search(pattern, username)
if matcht:
    print(f"El nombre de usuario '{username}' es válido.")
else:    print(f"El nombre de usuario '{username}' no es válido.")



#Buscar todas las vocales de una palabra


text = "Hola Mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text,)
print(f"Las vocales encontradas en '{text}' son: {matches}")

#Una regex para encontrar las palabras man, fan y ban, pero ignora el resto
text = "man ran fan ñan ban can"
patteng = r"[mfb]an"
matches = re.findall(patteng, text)
print(f"Las palabras encontradas en '{text}' son: {matches}")

# [^]  coincide con cualquier caracter que no este dentro de los corchetes
text = "Hola Mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(f"Los caracteres que no son vocales en '{text}' son: {matches}")