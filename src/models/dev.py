from models.funcionario import Funcionario

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    
    def calcular_bonus(self):
        taxa = 10
        bonus = (self.salario / 100) * taxa
    
        return f'R${bonus:,.2f}'

    
    def __str__(self):
        return super().__str__()