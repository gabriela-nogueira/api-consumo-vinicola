import requests
import csv
from io import StringIO
from fastapi import HTTPException


def get_dados_comercializacao():
    url = "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv"
    response = requests.get(url)

    csv_data = []

    header = ['id','produto','produto_2', *[str(x) for x in range(1970,2023)]]

    with StringIO(response.text) as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=header, delimiter=';')
        for row in reader:
            csv_data.append(dict(row))

    return csv_data

def get_dados_comercializacao_ano(ano: str):
    if (ano is not None):
        if (int(ano) < 1970 or int(ano) > 2022):
            raise HTTPException(status_code=404, detail="Ano informado não encontrado.")
        
    data = get_dados_comercializacao()

    dados_por_ano = [{'id': row['id'] , 'produto': row['produto'], ano: row[ano]} for row in data]

    return dados_por_ano