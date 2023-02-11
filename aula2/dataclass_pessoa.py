from datetime import date
from decimal import Decimal
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    cpf: str
    endereco: str
    dt_nascimento: date
    cep: str
    telefone: str


@dataclass
class Funcionario(Pessoa):
    cargo: str
    salario: Decimal
