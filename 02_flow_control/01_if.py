
import os
os.system("clear")

#Sentencias condicionales

edad = 18

if edad >= 18:
    print("Goat")
else: 
    print("Not goat")

#elif

nota = 0
if nota>=9:
    print("Felicidades, tienes un "+nota)
elif nota >=7:
    print("Not bad")
elif nota >=5:
    print("Por los pelos")
elif nota <=4:
    print("Haber estudiado crack!")
    print("Pa la proxima espabilas")
else:
    print("No te has presentado broski")


# Condicionales logicos
tiene_carnet = True;

if(edad<=18 and tiene_carnet):
    print("A conducir crack")

edad = 20

if edad >= 20:
    if tiene_carnet:
        print("Eres un maquina")
    else:
        print("Estudia crack")
else:
    print("No vales pa na")



print(5 != 3)
