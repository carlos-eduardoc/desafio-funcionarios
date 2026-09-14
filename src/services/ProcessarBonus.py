def processar_bonus(funcionario):
    try:
        print(funcionario.calcular_bonus())
    except AttributeError as ex:
        print(f'{ex}: O objeto não suporta ou não tem o metodo necessario')
    except ValueError as ex:
        print(f'{ex}: o objeto é um valor invalido')
    except TypeError as ex:
        print(f'{ex}: objeto da erro de tipagem')