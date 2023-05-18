import sys
import json
from process import Operacoes
import util

operacoes = Operacoes()

def carregar_json():
    arquivo_input = sys.argv[1]
    aux = sys.argv[1].split("\\")
    arquivo_output = aux[2]
    with open(arquivo_input, 'r') as j:
        conteudo = json.loads(j.read())
        for k in conteudo:
            if k["operation"] == "buy":
                imposto = operacoes.buy(k["quantity"], k["unit-cost"])
                util.gerar_arquivo_json(arquivo_output, imposto)
            if k["operation"] == "sell":
                resultado = operacoes.sell(k["quantity"], k["unit-cost"])
                util.gerar_arquivo_json(arquivo_output, resultado)
carregar_json()