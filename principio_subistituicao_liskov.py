from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, saldo: float):
        self.saldo = saldo

    @abstractmethod
    def pode_sacar(self, valor: float) -> bool:
        """Define a regra de negócio para permitir ou não o saque."""
        pass

    def sacar(self, valor: float) -> bool:
        if self.pode_sacar(valor):
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso. Saldo: R${self.saldo}")
            return True
        print(f"Saque de R${valor} recusado. Saldo insuficiente.")
        return False

class ContaCorrente(Conta):
    def pode_sacar(self, valor: float) -> bool:
        # Permite ficar negativo até -100
        return (self.saldo - valor) >= -100

class ContaSalario(Conta):
    def pode_sacar(self, valor: float) -> bool:
        # Não permite saldo negativo de forma alguma
        return (self.saldo - valor) >= 0

# A função do sistema agora funciona de forma segura com qualquer subclasse
def realizar_operacao_de_saque(conta: Conta):
    # O comportamento é previsível, nenhuma classe filha lança uma exceção surpresa
    conta.sacar(100)

# Testando a correção
cc = ContaCorrente(saldo=50)
realizar_operacao_de_saque(cc) # Sucesso (Saldo vai para -50)

cs = ContaSalario(saldo=50)
realizar_operacao_de_saque(cs) # Recusado com segurança, sem quebrar o código
