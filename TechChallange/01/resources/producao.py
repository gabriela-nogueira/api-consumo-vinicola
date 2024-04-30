import requests
import csv
from io import StringIO
from fastapi import HTTPException

""" Retorna os dados do arquivo de producao """  
def get_data_producao():
    url = "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"
    response = requests.get(url)

    csv_data = []

    with StringIO(response.text) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        for row in reader:
            csv_data.append(dict(row))

    return csv_data

""" Define metodo para recuperar dados a partir do ano """
def get_data_producao_ano(ano: str):

    if (ano is not None):
        if (int(ano) < 1970 or int(ano) > 2022):
            raise HTTPException(status_code=404, detail="Ano informado não encontrado.")
        
    data = get_data_producao()

    dados_por_ano = [{'id': row['id'] , 'produto': row['produto'], ano: row[ano]} for row in data]

    return dados_por_ano