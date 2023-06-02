class Animal:
    def som(self):
        print("Som dos animais")

class Cachorro(Animal):
    def som(self):
        print("Dog Au au")

class Gato(Animal):
    def som(self):
        print("Cat Miau")

animal1 = Cachorro()
animal2 = Gato()

animal1.som()
animal2.som()
