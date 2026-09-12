# Esse principio diz para você depender de abstrações e não de implementações.

from abc import ABC, abstractmethod


class CalcularDesconto(ABC):
    @abstractmethod
    def calcular_desconto(self, preco, desconto) -> float: ...


class CalcularDescontoFixo(CalcularDesconto):
    def calcular_desconto(self, preco, desconto) -> float:
        if desconto > preco:
            return 0.0

        return preco - desconto


class CalcularDescontoPercentual(CalcularDesconto):
    def calcular_desconto(self, preco, desconto) -> float:
        return (desconto + preco) / 100
