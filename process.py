class Operacoes:
    def __init__(self):
        self.quantidade_acoes = 0
        self.media_ponderada = 0
        self.prejuizo = 0

    def buy(self, quantidade, valor):
        nova_media_ponderada = ((self.quantidade_acoes * self.media_ponderada) + (quantidade * valor)) / (self.quantidade_acoes + quantidade)
        self.media_ponderada = nova_media_ponderada
        self.quantidade_acoes += quantidade
        return 0

    def sell(self, quantidade, valor):
        lucro = (valor - self.media_ponderada) * quantidade
        lucro -= self.prejuizo
        imposto_pago = 0
        if lucro > 0:
            if (valor * quantidade) > 20000:
                imposto_pago = lucro * 0.2
                lucro -= imposto_pago
            if self.prejuizo > 0:
                if lucro >= self.prejuizo:
                    lucro -= self.prejuizo
                    self.prejuizo = 0
                else:
                    self.prejuizo -= lucro
                    lucro = 0
        else:
            self.prejuizo -= lucro
            lucro = 0
        self.quantidade_acoes -= quantidade
        return imposto_pago