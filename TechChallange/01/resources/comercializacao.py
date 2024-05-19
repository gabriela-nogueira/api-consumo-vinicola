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
        next(reader) # Pular a primeira linha do CSV
        for row in reader:
            retorno = {
                "id": row["id"],
                "produto": row["produto"],
                "produto_2": row["produto_2"],
                "anos": {year: row[year] for year in header[3:]} # header[3:] para recuperar somente os anos
            }

            csv_data.append(retorno)

    return csv_data

def get_dados_comercializacao_ano(ano: str):
    if (ano is not None):
        if (int(ano) < 1970 or int(ano) > 2023):
            raise HTTPException(status_code=404, detail="Ano informado não encontrado.")
        
    data = get_dados_comercializacao()

    dados_por_ano = [{'id': row['id'], 'produto': row['produto'], 'produto_2': row['produto_2'], ano: row['anos'][ano]} for row in data]

    return dados_por_ano