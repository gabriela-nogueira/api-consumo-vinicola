from fastapi import FastAPI
from resources.processamento import get_processamento_tipo, get_processamento_ano

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/processamento/{tipo}")
async def processamento_tipo(tipo: str):
    """ Retorna o tipo de processamento entre os anos de 1970 até 2022 (qualquer valor diferente disso, irá retornar como erro)

    O parâmetro [tipo] deve ser enviado utilizando os números entre 1 e 4 (qualquer valor diferente disso, irá retornar como erro)

    Referência:
    {
        1: Viníferas
        2: Americanas e híbridas
        3: Uvas de mesa
        4: Sem classificação
    }
    """
    return get_processamento_tipo(tipo)

@app.get("/processamento/{tipo}/{ano}")
async def processamento_ano(tipo: str, ano: str):
    """ Retorna o tipo de processamento do ano informado

    O parâmetro [tipo] deve ser enviado utilizando os números entre 1 e 4 (qualquer valor diferente disso, irá retornar como erro)
    O parâmetro [ano] deve ser enviado entre 1970 e 2022 (qualquer valor diferente disso, irá retornar como erro)

    Referência:
    {
        1: Viníferas
        2: Americanas e híbridas
        3: Uvas de mesa
        4: Sem classificação
    }
    """

    return get_processamento_ano(tipo, ano)