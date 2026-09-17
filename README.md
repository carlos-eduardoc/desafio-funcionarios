<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="90" alt="Python logo"/>

# Desafio Funcionários — Classes Abstratas e Herança em Python

### Sistema de cálculo de bônus para diferentes cargos, usando POO com `abc`

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![POO](https://img.shields.io/badge/Paradigma-Orientado%20a%20Objetos-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)
![Licença](https://img.shields.io/badge/Licença-MIT-green?style=for-the-badge)

</div>

---

## Sobre este repositório

Este repositório resolve o desafio: criar uma classe abstrata `Funcionario`, com nome público e salário privado, contendo um método abstrato de cálculo de bônus. A partir dela, três cargos — `Gerente`, `Desenvolvedor` e `Designer` — implementam essa regra cada um com sua própria taxa.

O objetivo não é só fazer o bônus sair certo na tela, e sim treinar pilares de orientação a objetos que aparecem em qualquer sistema maior:

- **Classe abstrata** (`ABC`, `@abstractmethod`) para obrigar cada cargo a implementar seu próprio cálculo,
- **Encapsulamento** (atributo privado + `@property`/`@setter`) para proteger o salário de alterações inválidas,
- **Herança e polimorfismo** para reaproveitar o construtor da classe base e sobrescrever apenas o que muda entre cargos,
- **Tratamento de erros** para lidar com valores e tipos inválidos sem derrubar o programa.

Abaixo eu explico cada um desses pontos com trechos de código reais tirados do próprio repositório.

---

## Classe abstrata e encapsulamento

A classe `Funcionario`, em `src/models/funcionario.py`, define o contrato que todo cargo precisa seguir. `salario` é armazenado como atributo privado (`__salario`) e só é acessado através de uma `property`, que valida qualquer tentativa de alteração:

```python
class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor):
        if valor < self.__salario:
            raise ValueError('Você não pode reduzir o salario do funcionario')
        self.__salario = valor

    @abstractmethod
    def calcular_bonus(self):
        pass
```

Como `Funcionario` herda de `ABC` e declara `calcular_bonus` como `@abstractmethod`, ela não pode ser instanciada diretamente — só serve como base. Qualquer subclasse que não implementar `calcular_bonus` também não pode ser instanciada, o que garante que todo cargo tenha essa regra definida.

---

## Herança e polimorfismo

Cada cargo herda de `Funcionario`, reaproveita o `__init__` da classe base com `super()` e sobrescreve apenas `calcular_bonus`, cada um com sua própria taxa. Exemplo do `Desenvolvedor` (`src/models/dev.py`):

```python
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        taxa = 10
        bonus = (self.salario / 100) * taxa
        return f'R${bonus:,.2f}'
```

`Designer` e `Gerente` seguem exatamente a mesma estrutura, mudando só a `taxa` (8 e 15, respectivamente). É esse método sobrescrito que faz o polimorfismo funcionar: em `src/services/ProcessarBonus.py`, a função `processar_bonus` chama `funcionario.calcular_bonus()` sem precisar saber se recebeu um `Gerente`, um `Desenvolvedor` ou um `Designer` — cada objeto sabe calcular o próprio bônus.

---

## Tratamento de erros

O setter de `salario` lança um `ValueError` quando alguém tenta reduzir o salário de um funcionário. Esse erro é capturado tanto em `processar_bonus` quanto no `__main__.py`, para que uma tentativa inválida não interrompa o programa inteiro:

```python
def processar_bonus(funcionario):
    try:
        print(funcionario.calcular_bonus())
    except AttributeError as ex:
        print(f'{ex}: O objeto não suporta ou não tem o metodo necessario')
    except ValueError as ex:
        print(f'{ex}: o objeto é um valor invalido')
    except TypeError as ex:
        print(f'{ex}: objeto da erro de tipagem')
```

Tratar `AttributeError`, `ValueError` e `TypeError` separadamente deixa claro qual foi o problema — um objeto sem o método esperado, um valor fora da regra de negócio, ou um tipo incompatível — em vez de um único `except Exception` genérico que esconde a causa real.

---

## Estrutura do projeto

```
desafio-funcionarios/
├── src/
│   ├── __main__.py
│   ├── models/
│   │   ├── funcionario.py   # classe abstrata
│   │   ├── dev.py           # taxa de bonus: 10%
│   │   ├── designer.py      # taxa de bonus: 8%
│   │   └── gerente.py       # taxa de bonus: 15%
│   └── services/
│       └── ProcessarBonus.py
├── exercicio.txt
└── .gitignore
```

`__main__.py` instancia um funcionário de cada cargo, testa o aumento de salário e chama `processar_bonus` para cada um, imprimindo o resultado (ou o erro tratado) no terminal.

---

## Como executar

```bash
# clonar o repositório
git clone https://github.com/carlos-eduardoc/desafio-funcionarios.git
cd desafio-funcionarios

# instalar a única dependência externa (usada para inspeção/debug)
pip install rich

# executar o programa
python src/__main__.py
```
