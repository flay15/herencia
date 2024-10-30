class Animal:
    def hacer_sonido(self):
        return "Sonido genérico de animal"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

perro = Perro()
gato = Gato()

print(f"El perro dice: {perro.hacer_sonido()}")
print(f"El gato dice: {gato.hacer_sonido()}")
