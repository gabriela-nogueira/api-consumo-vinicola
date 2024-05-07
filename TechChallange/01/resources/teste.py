import requests
import csv
from io import StringIO

ano = "1970"
url = "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv"
response = requests.get(url)

csv_data = []

header = ['id','produto','produto_2', *range(1970,2023)]

with StringIO(response.text) as csv_file:
    reader = csv.DictReader(csv_file, fieldnames=header, delimiter=';')
    for row in reader:
        csv_data.append(dict(row))

dados_por_ano = [{'id': row['id'] , 'produto': row['produto'], ano: row[ano]} for row in csv_data]

csv_data