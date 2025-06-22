import os
os.system("clear")


lista1 = [1, 2, 3, 4, 5]
lista2 = ["pera", "manzana", "melon"]
lista3 = [1, "hola", 3.14, True]

lista_vacia = []
matriz = [[1, 2], [3, 4]]

#print(matriz)


lista_slice = [1, 2, 3, 4, 5]
# print(lista_slice[1:4])
# print(lista_slice[:3])
# print(lista_slice[3:])
# print(lista_slice[:])

#Más utilidades

lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
# print(lista1[::2]) #de 2 en 2

# print(lista1 [::-1]) #para devolver el array al reves

#modificar listas

# lista1[0] = "hola"
# print(lista1)



#añadir elementos

l1 = [1, 2, 3]
l1 = l1 + [4, 5, 6]

#mas eficiente

l1 += [7, 8, 9]
print(l1)