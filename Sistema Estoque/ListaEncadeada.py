class Nodo:

    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:

    def __init__(self):
        self.head = None

    def inserir(self, item):

        novoNodo = Nodo(item)

        if self.head is None:
            self.head = novoNodo
        else:

            atual = self.head

            while atual.proximo:
                atual = atual.proximo

            atual.proximo = novoNodo


    def listar(self):

        atual = self.head

        if atual is None:
            print("Lista vazia")
            return

        while atual:
            print(vars(atual.dado))
            atual = atual.proximo


    def buscar(self, idBuscar):

        atual = self.head

        while atual:

            # CAPIVARA
            if str(atual.dado.id) == str(idBuscar):
                return atual.dado

            atual = atual.proximo

        return None