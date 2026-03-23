class Venda:

    # Assim como Sheldon registra cada experimento em seus quadros
    def __init__(self, idVenda, cliente, produto, quantidade, valorTotal):

        self.id = idVenda
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.valor_total = valorTotal