import requests
import csv
from io import StringIO

""" Retorna url principal para download dos arquivos """
def get_url():
    return "http://vitibrasil.cnpuv.embrapa.br/download"

""" Retorna os dados do arquivo de processamento individualmente """
def get_data_processamento(file: str, delimiter: str, ano: str = None):

    if (ano is not None):
        if (int(ano) < 1970 or int(ano) > 2022):
            return "Ano informado é inválido"

    """ Le e seta retorno """
    url = f"{get_url()}/{file}.csv"
    response = requests.get(url, headers={'Accept-Charset': 'utf-8'})

    if (response.status_code == 200):

        """ Encoding """
        encoding = response.encoding
        response = response.content.decode(encoding)

        """ Cria dicionario """
        csv_data = []

        """ Le csv e concatena os dados do arquivo """
        with StringIO(response) as csv_file:
            reader = csv.DictReader(csv_file, delimiter = f"{delimiter}")
            for row in reader:
                if (ano is not None):
                    csv_data.append(dict({
                        "id": row["id"],
                        "control": row["control"],
                        "cultivar": row["cultivar"],
                        ano: row[ano]
                        }))
                else:
                    csv_data.append(dict(row))

        return csv_data

    else:
        return "Não foi possível ler o arquivo"

def get_data_importacao(file: str, delimiter: str, ano: str = None):
    if (ano is not None):
        if (int(ano) < 1970 or int(ano) > 2022):
            return "Ano informado é inválido"

    """ Le e seta retorno """
    url = f"{get_url()}/{file}.csv"
    response = requests.get(url, headers={'Accept-Charset': 'utf-8'})
    csv_data = []
    #csv_data.append({'id': index_aux + 1, 'tipo_importacao' : importacao})
    #url = f"http://vitibrasil.cnpuv.embrapa.br/download/Imp{importacao}.csv"
    #response = requests.get(url, headers={'Accept-Charset': 'latin-1'})

    fieldnames = ['id', 'pais'] + [f"{ano}_{coluna}" for ano in [str(x) for x in range(1970,2023)] for coluna in ['quantidade','valor']]

    with StringIO(response.text) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        for row in reader:
            if ano is not None:
                temp_dict = { chave.encode('latin-1').decode('utf-8'): valor.encode('latin-1').decode('utf-8') for chave, valor in dict(row).items()}
                temp_dict = {'id': temp_dict['Id'], 'País': temp_dict['País'], ano: temp_dict[ano]}
            else:
                temp_dict = { chave.encode('latin-1').decode('utf-8'): valor.encode('latin-1').decode('utf-8') for chave, valor in dict(row).items()}
            csv_data.append(temp_dict)
    
    return csv_data