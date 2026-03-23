class Pilha:

    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):

        if len(self.itens) == 0:
            return None

        return self.itens.pop()

    def vazia(self):
        return len(self.itens) == 0