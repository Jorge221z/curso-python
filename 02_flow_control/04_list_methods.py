import os
os.system("clear")


lista = ['a', 'b', 'c', 'd']

lista.append('e')
print(lista)

lista.insert(1, '@')      #inserta un elemento en la posicion que le indiquemos
print(lista)

lista.extend(['z', 'x'])
print(lista)

lista.remove('@')
print(lista)

lista.pop() #eliminar el ultimo elemento de la lista y ademas lo devuelve(tambien se le pueden pasar indices concretos)
print(lista)

del lista[-1]   #eliminamos ultimo elemento de la lista
print(lista)

del lista[0:2]   #tambien podemos especificar un rango
print(lista)

lista.clear()    #eliminar todos los elementos de la lista
print(lista)



numeros = [2, 5, 6, 7, 1]

numeros.sort()   # modifica la lista original, no la devuelve como tal 
print(numeros)


numeros = [2, 5, 6, 7, 1]
sorted_numbers = sorted(numeros) #con sorted lo hacemos igual pero con una lista
print(sorted_numbers)


#si queremos ordenar una lista de cadenas de texto:
frutas = ['pera', 'manzana', 'naranja', 'kiwi']

sorted_fruits = sorted(frutas)  # ordena alfabéticamente
print(sorted_fruits)


#si queremos ordenar una lista de cadenas de texto que no sea todo en minusculas:
frutas = ['Pera', 'manzana', 'Naranja', 'kiwi']

frutas.sort(key=str.lower)  # ordena ignorando mayúsculas y minúsculas

print(frutas)


animales = ['perro', 'gato', 'elefante', 'jirafa']
print(len(animales))  # longitud de la lista
print(animales.count("perro"))

print('gato' in animales) #devuelve un booleano(True o False)