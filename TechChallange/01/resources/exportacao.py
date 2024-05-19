import requests
import csv
from io import StringIO


""" Define metodo para recuperar dados  """
def get_exportacao_tipo(tipo: str):
    dict_tipo = {
        "1" : "ExpVinho",
        "2" : "ExpEspumantes",
        "3" : "ExpUva",
        "4" : "ExpSuco",
    }
    return get_data_exportacao(dict_tipo[tipo])

def get_importacao_ano(tipo: str, ano: str):
    dict_tipo = {
        "1" : "ImpVinhos",
        "2" : "ImpEspumantes",
        "3" : "ImpFrescas",
        "4" : "ImpPassas",
        "5" : "ImpSuco"
    }
    return get_data_exportacao(dict_tipo[tipo], ano)

def get_exportacao():
    tipos_exportacao = ['Vinho','Espumantes','Uva', 'Suco']

    header = ['id', 'pais'] + [f"{ano}_{coluna}" for ano in [str(x) for x in range(1970,2023)] for coluna in ['quantidade','valor']]
    
    csv_data = []

    for exportacao in tipos_exportacao:
        index_aux = tipos_exportacao.index(exportacao)
        csv_data.append({'id': index_aux + 1, 'tipo_exportacao' : exportacao})
        url = f"http://vitibrasil.cnpuv.embrapa.br/download/Exp{exportacao}.csv"
        response = requests.get(url, headers={'Accept-Charset': 'latin-1'})

        with StringIO(response.text) as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=header, delimiter=';')
            next(reader)
            #next(reader)
            for row in reader:
                initial_dict = {'id' : row['id']}
                temp_dict = {str(ano): {"quantidade" : row[f'{ano}_quantidade'], "valor" : row[f"{ano}_valor"]} for ano in range(1970,2023)}
                initial_dict.update(temp_dict)
                csv_data[tipos_exportacao.index(exportacao)].update({row['pais']: initial_dict})

    return csv_data

def get_data_exportacao(file: str, ano: str = None):
    
    if (ano is not None):
        if (int(ano) < 1970 or int(ano) > 2023):
            return "Ano informado é inválido"

    dados = get_exportacao()

    csv_data = [{key: value for key,value in row.items() if row['tipo_exportacao'] == file[3:]} for row in dados]

    csv_data = [temp_dict for temp_dict in csv_data if temp_dict]
    
    return csv_data