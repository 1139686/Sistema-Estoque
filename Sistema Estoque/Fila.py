class Fila:

    def __init__(self):
        self._itens = []

    def enfileirar(self, item):
        self._itens.append(item)

    def desenfileirar(self):

        # CAPIVARA
        if self.esta_vazia():
            print("Fila vazia")
            return None

        return self._itens.pop(0)

    def esta_vazia(self):
        return len(self._itens) == 0

    def tamanho(self):
        return len(self._itens)

    def listar(self):

        if self.esta_vazia():
            print("Nenhuma venda registrada")
            return

        for item in self._itens:
            print(vars(item))