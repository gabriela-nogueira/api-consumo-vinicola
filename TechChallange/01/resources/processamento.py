import requests
import csv
from io import StringIO
from resources.embrapa import get_data_processamento

""" Define metodo para recuperar dados  """
def get_processamento_tipo(tipo: str):
    if tipo == "1":
        return get_data_processamento("ProcessaViniferas", "\t")
    elif tipo == "2":
        return get_data_processamento("ProcessaAmericanas", "\t")
    elif tipo == "3":
        return get_data_processamento("ProcessaMesa", "\t")
    elif tipo == "4":
        return get_data_processamento("ProcessaSemclass", "\t")
    else:
        return "Tipo de processamento inválido"

def get_processamento_ano(tipo: str, ano: str):
    if tipo == "1":
        return get_data_processamento("ProcessaViniferas", "\t", ano)
    elif tipo == "2":
        return get_data_processamento("ProcessaAmericanas", "\t", ano)
    elif tipo == "3":
        return get_data_processamento("ProcessaMesa", "\t", ano)
    elif tipo == "4":
        return get_data_processamento("ProcessaSemclass", "\t", ano)
    else:
        return "Tipo de processamento inválido"

def get_processamento():
    tipos_processamento = ['Viniferas','Americanas','Mesa','Semclass']
    csv_data = []

    for processamento in tipos_processamento:
        index_aux = tipos_processamento.index(processamento)
        csv_data.append({'id_processamento': index_aux + 1, 'tipo_processamento' : processamento})
        url = f"http://vitibrasil.cnpuv.embrapa.br/download/Processa{processamento}.csv"
        response = requests.get(url, headers={'Accept-Charset': 'latin-1'})

        with StringIO(response.text) as csv_file:
            reader = csv.DictReader(csv_file, delimiter='\t')
            for row in reader:
                data = {}
                data.update(dict({key : value.encode('latin-1').decode('utf-8') for key, value in row.items()}))
                csv_data[tipos_processamento.index(processamento)].update({f"data_{data['control']}": data})

    return csv_data