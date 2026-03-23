from ListaEncadeada import ListaEncadeada
from Fila import Fila
from Pilha import Pilha

class SistemaEstoque:

    def __init__(self):

        self.produtos = ListaEncadeada()
        self.clientes = ListaEncadeada()

        self.vendas = Fila()

        self.historico = Pilha()