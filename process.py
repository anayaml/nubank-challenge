class Processo:

    def __init__(self, custo_unidade, operacao, quantidade):
        self.custo_unidade = custo_unidade
        self.operacao = operacao
        self.quantidade = quantidade

def comprar_acoes():
    return 0

def vender_acoes():
    return 0

def calcular_peso_medio_ponderado(qtd_atual_acoes, media_ponderada_atual, qtd_acoes_compradas, valor_compra):
    return ((qtd_atual_acoes * media_ponderada_atual) + (qtd_acoes_compradas * valor_compra)) / (qtd_atual_acoes + qtd_acoes_compradas)

def calcular_taxa_operacao(custo_unidade_acao, peso_medio_moderado_atual, qtd_acoes):
    valor_total = custo_unidade_acao * qtd_acoes
    return custo_unidade_acao > peso_medio_moderado_atual and valor_total > 20000

def calcular_prejuizo_acao(custo, peso_medio_moderado_atual):
    return custo < peso_medio_moderado_atual