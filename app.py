import sys
import json
import process

def carregar_json():
    file_name = sys.argv[1]
    with open(file_name, 'r') as j:
        conteudo = json.loads(j.read())
        


carregar_json()