class Animal:
    def __init__(self, nome):
        self.nome = nome

    def som(self):
        pass


class Dog(Animal):
    def som(self):
        return "Au au!"

class Cat(Animal):
    def som(self):
        return "Miau!"


boby = Dog("Boby")
print(boby.nome)
print(boby.som())

bills = Cat("Bills")
print(bills.nome)
print(bills.som())
