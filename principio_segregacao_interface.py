# Uma classe não pode herdar um metodo que nunca vai ser implementado

from abc import ABC, abstractmethod


class Produto(ABC):

    @abstractmethod
    def gerar_link(self): ...


    @abstractmethod
    def calcular_total(self): ...


class ProdutoFisico(ABC):

    @abstractmethod
    def calcular_frete(self): ...


class GuiaAlimentarParaAtletas(Produto):

    def gerar_link(self):
        return 'https://plataforma.com.br/guiaalimentar/'

    def calcular_total(self):
        return 29.90


class MarmitasFit(Produto, ProdutoFisico):
    def gerar_link(self):
            return 'https://guiaalimentar.com.br/marmitas/'
    
    def calcular_total(self):
        return 'Total das marmitas + frete'

    def calcular_frete(self):
         return 'Total do frete'
