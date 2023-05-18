import sys
import json
from process import Operacoes

operacoes = Operacoes()

def carregar_json():
    file_name = sys.argv[1]
    with open(file_name, 'r') as j:
        conteudo = json.loads(j.read())
        for k in conteudo:
            if k["operation"] == "buy":
                imposto = operacoes.buy(k["quantity"], k["unit-cost"])
                print(imposto)
            if k["operation"] == "sell":
                resultado = operacoes.sell(k["quantity"], k["unit-cost"])
                print(resultado)
carregar_json()