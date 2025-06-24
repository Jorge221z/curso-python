import os
os.system("clear")



# contador = 0
# while contador <= 5:
#     print(contador)
#     contador += 1


# while True:
#     print(contador)
#     contador += 1
#     if contador == 1000:
#         break

#bloque continue

# contador = 0
# while contador < 10:
#     contador += 1
#     if contador % 2 == 0:
#         continue   # nos saltamos el print del contador cuando es multiplo de 2 (osea que da resto 0)

#     print(contador)


# contador = 0
# while contador < 10:
#     contador += 1
# else:      #lo que pongamos despues del else solo se ejecutará una vez hemos salido del bucle excepto si hemos usado break
#     print("Fin del bucle")



#Ejercicio practico
#Pedimos un numero al usuario, y mientras no sea positivo no dejaremos de pedirlo

# num = int(input("Dame un numero\n"))

# while num < 0:
#     num = int(input("Dame un numero positivo\n"))
# else:
#     print(f"Por fin me das un numero positivo: {num}")


num = int(input("Dame un numero\n"))

while num < 0:
    try:
        num = int(input("Dame un numero positivo\n"))
    except:
        print("No has introducido un entero")
else:
    print(f"Por fin me das un numero positivo: {num}")