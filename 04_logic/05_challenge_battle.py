from os import system
if system("clear") != 0: system("cls")

"""
Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud. 

Cada número en lista_a se "enfrenta" al número en la misma posición en lista_b.

- Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
- Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
- Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.

Debes simular estos enfrentamientos y devolver el resultado final:
- Si al final queda un número en lista_a, devuelve ese número seguido de la letra "a" (por ejemplo, "3a").
- Si al final queda un número en lista_b, devuelve ese número seguido de la letra "b" (por ejemplo, "2b").
- En caso de empate, devuelve la letra "x".

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

resultado = battle(lista_a, lista_b)  # -> "2b"

# Explicación:
# - 2 vs 3: gana 3 (+1)
# - 4 vs 3+1: empate
# - 2 vs 4: gana 4 (+2)
# Resultado: "2b"

lista_a = [4, 4, 4]
lista_b = [2, 8, 2]

resultado = battle(lista_a, lista_b)  # -> "x"

# Explicación:
# - 4 vs 2: gana 4 (+2)
# - 4+2 vs 8: gana 8 (+2)
# - 4 vs 2+2: empate
# Resultado: "x"
"""



def battle(lista_a, lista_b):
    diferencia = 0
    ganador = 0
    empate = False
    for i, num in enumerate(range(len(lista_a)-1)):
        if lista_a[i] > lista_b[i]:
            diferencia = lista_a[i] - lista_b[i] #es la diferencia actual, pero nos sirve como referencia
            lista_a[i+1] = lista_a[i+1] + diferencia
            

        elif lista_b[i] > lista_a[i]:
            diferencia = lista_b[i] - lista_a[i]
            lista_b[i+1] = lista_b[i+1] + diferencia

        elif lista_a[i] == lista_b[i]:
            continue
            
    
    if lista_a[-1] > lista_b[-1]:
        print(f"{lista_a[-1]}a")
    elif lista_b[-1] > lista_a[-1]:
        print(f"{lista_b[-1]}b")
    elif lista_a[-1] == lista_b[-1]:
        print("X")

lista_a = [2, 3, 3]
lista_b = [3, 12, 4]


resultado = battle(lista_a, lista_b)  # -> "2b"