from resources.embrapa import get_data

""" Define metodo para recuperar dados  """
def get_processamento_tipo(tipo: str):
    if tipo == "1":
        return get_data("ProcessaViniferas", "\t")
    elif tipo == "2":
        return get_data("ProcessaAmericanas", "\t")
    elif tipo == "3":
        return get_data("ProcessaMesa", "\t")
    elif type == "4":
        return get_data("ProcessaSemclass", "\t")
    else:
        return "Tipo de processamento inválido"

def get_processamento_ano(tipo: str, ano: str):
    if tipo == "1":
        return get_data("ProcessaViniferas", "\t", ano)
    elif tipo == "2":
        return get_data("ProcessaAmericanas", "\t", ano)
    elif tipo == "3":
        return get_data("ProcessaMesa", "\t", ano)
    elif type == "4":
        return get_data("ProcessaSemclass", "\t", ano)
    else:
        return "Tipo de processamento inválido"