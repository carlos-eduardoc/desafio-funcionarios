from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self._salario = salario
    
    def __str__(self):
        return f'O {self.__class__.__name__} tem o salario de R${self.salario:,.2f} e por ser {self.__class__.__name__} tem o bonus de {self.calcular_bonus()}'
    
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, valor):
        if valor < self._salario:
            raise ValueError('Você não pode reduzir o salario do funcionario')
        self.__salario = valor
    
    
    @abstractmethod
    def calcular_bonus(self):
        pass