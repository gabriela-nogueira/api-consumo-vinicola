import requests
import csv
from io import StringIO
from resources.embrapa import get_data_processamento


""" Define metodo para recuperar dados  """
def get_importacao_tipo(tipo: str):
    if tipo == "1":
        return get_data_processamento("ImpVinhos", "\t")
    elif tipo == "2":
        return get_data_processamento("ImpEspumantes", "\t")
    elif tipo == "3":
        return get_data_processamento("ImpFrescas", "\t")
    elif tipo == "4":
        return get_data_processamento("ImpPassas", "\t")
    elif tipo == "5":
        return get_data_processamento("ImpSuco", "\t")
    else:
        return "Tipo de processamento inválido"

def get_importacao_ano(tipo: str, ano: str):
    if tipo == "1":
        return get_data_processamento("ImpVinhos", "\t", ano)
    elif tipo == "2":
        return get_data_processamento("ImpEspumantes", "\t", ano)
    elif tipo == "3":
        return get_data_processamento("ImpFrescas", "\t", ano)
    elif tipo == "4":
        return get_data_processamento("ImpPassas", "\t", ano)
    elif tipo == "5":
        return get_data_processamento("ImpSuco", "\t", ano)
    else:
        return "Tipo de processamento inválido"

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