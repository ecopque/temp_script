class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    @property
    def motor(self):
        return self._motor
    @motor.setter
    def motor(self, valor):
        self._motor = valor
    @property
    def fabricante(self):
        return self._fabricante
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
class Motor:
    def __init__(self, nome):
        self.nome = nome
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
fusca = Carro(nome='Fusca')
corolla = Carro(nome='Corolla')
motor10 = Motor(nome='1.0')
motor20 = Motor(nome='2.0')
fab = Fabricante(nome='Volks')


fusca.motor10 = motor10
fusca.motor20 = motor20
fusca.montadora = fab

print(fusca.nome, fusca.motor10.nome, fusca.montadora.nome)
print(corolla.nome, motor20.nome)