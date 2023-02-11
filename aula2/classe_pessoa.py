from datetime import date
from decimal import Decimal


class Pessoa:
    def __init__(self,
                 nome: str,
                 cpf: str,
                 endereco: str,
                 dt_nascimento: date,
                 cep: str,
                 telefone: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.dt_nascimento = dt_nascimento
        self.cep = cep
        self.telefone = telefone

    def consultar_cpf(self):
        pass


class Cliente(Pessoa):
    def __init__(self,
                 nome: str,
                 cpf: str,
                 endereco: str,
                 dt_nascimento: date,
                 cep: str,
                 telefone: str,
                 renda: Decimal) -> None:
        super().__init__(nome, cpf, endereco, dt_nascimento, cep, telefone)
        self.renda = renda

    def consultar_credito(self):
        pass


class Funcionario(Pessoa):
    def __init__(self,
                 nome: str,
                 cpf: str,
                 endereco: str,
                 dt_nascimento: date,
                 cep: str,
                 telefone: str,
                 salario: Decimal,
                 cargo: str) -> None:
        super().__init__(nome, cpf, endereco, dt_nascimento, cep, telefone)
        self.salario = salario
        self.cargo = cargo

    def marcar_ponto(self):
        pass


gabriel = Cliente("gabriel", "aaa", "Aaaa", "10/10/1203", "aaa", "aaaa", 1230)

print(gabriel.consultar_cpf())
