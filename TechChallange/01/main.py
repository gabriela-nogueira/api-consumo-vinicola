from fastapi import FastAPI
from resources.processamento import get_processamento_tipo, get_processamento, get_processamento_tipo_ano
from resources.producao import get_data_producao, get_data_producao_ano
from resources.comercializacao import get_dados_comercializacao, get_dados_comercializacao_ano
from resources.importacao import get_importacao, get_importacao_ano, get_importacao_tipo

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/importacao')
async def importacao():
    return get_importacao()

@app.get('/importacao/{tipo}')
async def importacao_tipo(tipo: str):
    return get_importacao_tipo(tipo)

@app.get('/importacao/{tipo}/{ano}')
async def importacao_ano(tipo: str, ano: str):
    return get_importacao_ano(tipo, ano)

@app.get("/processamento")
async def processamento():
    """ Retorna todos o processamento entre os anos de 1970 até 2022 (qualquer valor diferente disso, irá retornar como erro)"""
    return get_processamento()

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
async def processamento_tipo_ano(tipo: str, ano: str):
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

    return get_processamento_tipo_ano(tipo, ano)

@app.get("/processamento_ano/{ano}")
async def processamento(ano: str):
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

    return get_processamento(ano)

@app.get("/producao")
async def get_producao():
    """ Retorna toda a produção entre os anos de 1970 e 2023 (qualquer valor diferente disso, irá retornar como erro)"""
    return get_data_producao()

@app.get("/producao/{ano}")
async def get_producao(ano: str):
    """ Retorna a producao do ano informado que precisa estar entre os anos de 1970 até 2022 (qualquer valor diferente disso, irá retornar como erro)"""
    return get_data_producao_ano(ano)

@app.get("/comercializacao")
async def get_comercializacao():
    return get_dados_comercializacao()

@app.get("/comercializacao/{ano}")
async def get_comercializacao(ano: str):
    return get_dados_comercializacao_ano(ano)

# adicionando para testes 
if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)