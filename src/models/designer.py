from models.funcionario import Funcionario

class Designer(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        
    
    def calcular_bonus(self):
        taxa = 8
        bonus = (self._salario / 100) * taxa
            
        return f'R${bonus:,.2f}' 