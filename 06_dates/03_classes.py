# Las clases son plantillas para crear objetos
# Un objeto es una instacia de una clase


#Ejemplo basico

class Coche:
    tipo = "vehiculo de 4 ruedas"


    def __init__(self, marca, modelo, color): #self se refiere a si mismo
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} arrancó!")



mi_coche = Coche("BMW", "Z3", "Azul")
mi_coche.arrancar();


su_coche = Coche("Honda", "Civic", "Rojo")
su_coche.arrancar();