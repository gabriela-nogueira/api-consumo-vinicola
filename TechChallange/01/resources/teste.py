import requests
import csv
from io import StringIO

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

csv_data