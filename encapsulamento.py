class Carro:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def get_marca(self):
        return self.__marca

    def set_marca(self, nova_marca):
        self.__marca = nova_marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, novo_modelo):
        self.__modelo = novo_modelo


meu_carro = Carro("Fiat", "Uno")
print(meu_carro.get_marca())

meu_carro.set_marca("Chevrolet")
print(meu_carro.get_marca())

print(meu_carro.__marca)
