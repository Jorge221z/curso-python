from os import system
if system("clear") != 0: system("cls")


import re

text = "Hola mundo, H0la de nuevo, H0la otra vez"

pattern = "H.la" #el . vale por cualquier caracter, excepto salto de linea

found = re.findall(pattern, text)

if (found):
    print(found)
else:
    print("No hemos encontrado nada")



text = "casa caasa cosa cisa cesa causa"

pattern = "c.sa"

matches = re.findall(pattern, text)

print(matches)



text = "Hola mundo, H0la de nuevo, H0la otra vez"

pattern = r"H.la" #el . vale por cualquier caracter, excepto salto de linea

found = re.findall(pattern, text)

if (found):
    print(found)
else:
    print("No hemos encontrado nada")

#--------------------------------------------------

text = "Mi casa es blanca. Y el coche es negro"
pattern = r"\."  #con la barra cancelamos el comportamiento por defecto del punto. La r es opcional

matches = re.findall(pattern, text)

print(matches)



#--------------------------------------------------
# \d  coincide con cualquier digito entre 0 y 9

text = "El numero de telefono es 123456789"
found = re.findall(r'\d{9}', text)

print(found)


text = "Mi numero de telefono es +34 688999444, apuntalo vale?"

pattern = r"\+34 \d{9}"

found = re.search(pattern, text)

if found: print(f"Encontré el número de telefono {found.group()}")


#--------------------------------------------------
# \w  coincide con cualquier caracter alfanumerico

text = "el_rubius_69"

pattern = r"\w"

found = re.findall(pattern ,text)

print(found)


#--------------------------------------------------
# \s  coincide con cualquier espacio en blanco(espacio, tabulacion,salto de linea)

text = "Hola mundo\n, ¿Cómo estás?"

pattern = r"\s"

matches = re.findall(pattern, text)
print(matches)



#--------------------------------------------------
# ^  coincide con cualquier principio de una cadena
text = "423_name"

pattern = r"^\w"     #validar nombre de usuario

valid = re.search(pattern, text)

if valid:
    print("El nombre de usuario es válido")
else:
    print("El nombre de usuario no es válido")



#--------------------------------------------------
numero = "+34 688999444"
pattern = r"^\+\d{1,3} "  #validar numero de telefono

valid = re.search(pattern, numero)
if valid:
    print("El número de teléfono es válido")
else:
    print("El número de teléfono no es válido") 



#--------------------------------------------------
# $  coincide con cualquier final de una cadena
text = "Hola mundo"
pattern = r"mundo$"  #validar que la cadena termina con "mundo"

valid = re.search(pattern, text)
if valid:
    print("La cadena termina con 'mundo'")
else:
    print("La cadena no termina con 'mundo'")


#--------------------------------------------------
#Ejercicio, validar que un correo sea de gmail
email = "jorge221z@gmail.com"
pattern = r"@gmail.com$"

valid = re.search(pattern, email)
if valid:
    print("El correo es de Gmail")
else:
    print("El correo no es de Gmail")