# Uma classe tem que estar aberta para expansão e fechada para modificação

from abc import ABC, abstractmethod


class Pagamento(ABC):
    @abstractmethod
    def pagar(self): pass


class PagamentoCartaoCredito(Pagamento):
    def pagar(self):
        print("Pagamento com cartão de credito")


class PagamentoCartaoDebito(Pagamento):
    def pagar(self):
        print("Pagamento com cartão de debito")


class PagamentoPix(Pagamento):
    def pagar(self):
        print("Pagamento com pix")


forma_pagamento = PagamentoPix()
forma_pagamento.pagar()