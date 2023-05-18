import json

def gerar_arquivo_json(arquivo, valor):
    resultado = {
        "tax" : valor
    }
    json_output = json.dumps(resultado, indent=4)
    with open("output\\"+ arquivo,'a+') as f:
        f.write(json_output)
        f.write(",")