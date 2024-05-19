import requests
import csv
from io import StringIO
from fastapi import HTTPException

""" Retorna os dados do arquivo de producao """  
def get_data_producao():
    url = "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"
    response = requests.get(url)
    response.encoding = "utf-8"

    csv_data = {}

    with StringIO(response.text) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        for row in reader:

            # Adicionar inicio do dicionario
            id_value = row.pop("id")
            control_value = row.pop("control")
            produto_value = row.pop("produto")

            # Verificar se o id ja existe no dicionario, se nao, adiciona
            if id_value not in csv_data:
                csv_data[id_value] = {
                    "id": id_value,
                    "control": control_value,
                    "produto": produto_value,
                    "anos": {}
                }

            # Adicionar valores ao dicionario de anos
            dict_anos = csv_data[id_value]['anos']
            for key, value in row.items():
                dict_anos[key] = value

    return csv_data

""" Define metodo para recuperar dados a partir do ano """
def get_data_producao_ano(ano: str):

    if (ano is not None):
        if (int(ano) < 1970 or int(ano) > 2023):
            raise HTTPException(status_code=404, detail="Ano informado não encontrado.")
        
    data = get_data_producao()

    dados_por_ano = []
    for row in data.values():
        if ano in row['anos']:
            dados_por_ano.append(
                {'id': row['id'], 'control': row['control'], 'produto': row['produto'], ano: row['anos'][ano]})

    return dados_por_ano