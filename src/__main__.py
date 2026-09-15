from models.funcionario import Funcionario
from models.dev import Desenvolvedor
from models.designer import Designer
from models.gerente import Gerente
from services.ProcessarBonus import processar_bonus
from rich import inspect


def main():
    f1 = Desenvolvedor('Carlos', 3000)
    f2 = Designer('Joana', 2800)
    f3 = Gerente('Fabio', 5500)
    
    f1.salario = 4000
    inspect(f1, private=True, methods=True)
        
    f2.salario = 3020
    inspect(f2, private=True, methods=True)
    
    print('-' * 5 + 'DESENVOLVEDOR' + '-' * 5)
    try:
        processar_bonus(f1)
        print(f1)
    except Exception as ex:
        print(ex)
    
    print('\n')
    print('-' * 5 + 'DESIGNER' + '-' * 5)
    try:
        processar_bonus(f2)
        print(f2)
    except Exception as ex:
        print(ex)
      
    print('\n')
    print('-' * 5 + 'GERENTE' + '-' * 5)  
    try:
        processar_bonus(f3)
        print(f3)
    except Exception as ex:
        print(ex)
    
    

if __name__ == '__main__':
    main()