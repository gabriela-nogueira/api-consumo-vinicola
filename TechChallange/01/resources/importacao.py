import requests
import csv
from io import StringIO
from resources.embrapa import get_data_processamento, get_data_importacao


""" Define metodo para recuperar dados  """
def get_importacao_tipo(tipo: str):
    dict_tipo = {
        "1" : "ImpVinhos",
        "2" : "ImpEspumantes",
        "3" : "ImpFrescas",
        "4" : "ImpPassas",
        "5" : "ImpSuco"
    }
    return get_data_importacao(dict_tipo[tipo], ";")

def get_importacao_ano(tipo: str, ano: str):
    dict_tipo = {
        "1" : "ImpVinhos",
        "2" : "ImpEspumantes",
        "3" : "ImpFrescas",
        "4" : "ImpPassas",
        "5" : "ImpSuco"
    }
    return get_data_importacao(dict_tipo[tipo], ";", ano)

def get_importacao():
    tipos_importacao = ['Vinhos','Espumantes','Frescas','Passas', 'Suco']
    csv_data = []

    for importacao in tipos_importacao:
        index_aux = tipos_importacao.index(importacao)
        csv_data.append({'id': index_aux + 1, 'tipo_importacao' : importacao})
        url = f"http://vitibrasil.cnpuv.embrapa.br/download/Imp{importacao}.csv"
        response = requests.get(url, headers={'Accept-Charset': 'latin-1'})

        with StringIO(response.text) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            for row in reader:
                temp_dict = { chave.encode('latin-1').decode('utf-8'): valor.encode('latin-1').decode('utf-8') for chave, valor in dict(row).items()}
                csv_data[tipos_importacao.index(importacao)].update({f"{temp_dict['Id']}_{temp_dict['País']}": temp_dict})

    return csv_data