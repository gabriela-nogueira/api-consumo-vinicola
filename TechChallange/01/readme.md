# TechChallenge 01 - API Embrapa

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

Esta API foi desenvolvida como parte do trabalho tech challenge da pós-graduação em Engenharia de Machine Learning. Ela foi projetada para ler os dados a partir de um CSV do site da Embrapa e disponibiliza-los de acordo com tema pelas rotas definidas.

## Objetivo do Projeto

O principal objetivo desta API é facilitar a coleta, armazenamento e manipulação de dados que são disponibilizados em um site que contém as informações sobre produção de vinhos, sucos e derivados provenientes do Rio Grande do Sul. Para isso, foi criado as rotas necessárias sobre cada aba do site que englobam: Produção, Processamento, Comercialização, Importação e Exportação.

## Índice

- [Instalação](#instalação)
- [Uso](#uso)
- [Endpoints](#endpoints)
  - [GET /producao](#get-producao)
  - [GET /producao/[tipo]](#get-producao-tipo)
  - [GET /producao/[tipo]/[ano]](#get-producao-tipo)
- [Autenticação](#autenticação)
- [Erros](#erros)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Instalação

Instruções sobre como instalar e configurar a API.  

### Pré-requisitos

- Python (versão 3.9 ou superior)
- pip (gerenciador de pacotes do Python)
- Git (para clonar o repositório)
- FastAPI

Siga como base o arquivo de requerimentos disponível na pasta 01.

### Passo a Passo

1. **Clone o repositório:**

```sh
git clone https://github.com/AmorimVinicius/Machine-Learning-Engineering.git
cd Machine-Learning-Engineering/TechChallenge/01
```

2. **Crie um ambiente virtual:**

Como boa prática, utilize um ambiente virtual para isolar as dependências desse projeto.

```sh
python -m venv venv 
```

3. **Ative o ambiente virtual:** 

    - No Windows:
        ```sh
        venv\Scripts\activate
        ```
    
    - No macOs/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Instale as dependências:**

```sh
pip install -r requirements.txt
```

5. **Inicie a aplicação**

```sh
python main.py
```

A aplicação estará em execução em **'http:/localhost:8000'**.

## Uso

Quando trata-se de machine learning, em diversos cenários podemos utilizar as informações sobre o conteúdo disponibilizado na API. Alguns dos cenários possíveis:

- **Previsão de Demanda**: Utilizando dados históricos de produção e vendas, é possível treinar um modelo de machine learning para prever a demanda futura por diferentes tipos de bebidas. Esse tipo de previsão pode ajudar os produtores a ajustar suas operações de produção e estoque, minimizando desperdícios e maximizando a eficiência. Com os dados de produção, comercialização, importação e exportação o modelo pode identificar quais os produtos mais vendidos e as quantidades, conseguindo assim elaborar um plano de produção mais acertivo com base nos dados históricos.  
  

- **Otimização da Produção**: Com os dados é possível identificar os produtos que mais vendem e focar a produção nesses produtos chave, onde que otimiza a produção e também otimiza a cadeia de suprimentos. 

## Endpoints


### GET /producao

**Descrição**: Este endpoint retorna dados detalhados sobre a produção de vinhos, incluindo volumes de produção para cada tipo de vinho e subcategoria de vinho.

**Parâmetros**: não tem.

**Exemplo de Requisição:**

```sh
curl -X GET ""http://localhost:8000/producao"
```

**Resposta:**

```json
{
  "1": {
    "id": "1",
    "control": "VINHO DE MESA",
    "produto": "VINHO DE MESA",
    "anos": {
      "1970": "217208604",
      "1971": "154264651",
      "1972": "146953297",
      "1973": "116710345",
      "1974": "193875345",
      "1975": "177401209",
      ...
    }
  }
}
```

### GET /producao/[tipo]

**Descrição**: Este endpoint retorna o tipo de processamento entre os anos de 1970 até 2022 (qualquer valor diferente disso, irá retornar como erro)

O parâmetro [tipo] deve ser enviado utilizando os números entre 1 e 4 (qualquer valor diferente disso, irá retornar como erro)

**Referência**:

- 1: Viníferas
- 2: Americanas e híbridas
- 3: Uvas de mesa
- 4: Sem classificação

**Parâmetros**:

|   Parâmetro   |   Tipo   |   Descricao   |
|---------------|----------|---------------|
| Tipo          | String   | Tipo do processamento das referências |

**Exemplo de Requisição:**

```sh
curl -X GET ""http://localhost:8000/producao/1"
```

**Resposta:**

```json
{
  "1": {
    "id": "1",
    "control": "VINHO DE MESA",
    "produto": "VINHO DE MESA",
    "anos": {
      "1970": "217208604",
      "1971": "154264651",
      "1972": "146953297",
      "1973": "116710345",
      "1974": "193875345",
      "1975": "177401209",
      ...
    }
  }
}
```

**ATENÇÃO** Rever essa rota, deu um probleminha.

### GET /processamento

**Descrição**: Este endpoint retorna dados detalhados sobre a quantidade em kg de uvas processadas no Rio Grande do Sul do ano de 1970 a 2022.

**Parâmetros**: não tem.

**Exemplo de Requisição:**

```sh
curl -X GET ""http://localhost:8000/processamento"
```

**Resposta:**

```json
{
  "1": {
    "id": "1",
    "control": "VINHO DE MESA",
    "produto": "VINHO DE MESA",
    "anos": {
      "1970": "217208604",
      "1971": "154264651",
      "1972": "146953297",
      "1973": "116710345",
      "1974": "193875345",
      "1975": "177401209",
      ...
    }
  }
}
```

## Contribuição

Este trabalho foi elaborado em equipe e os alunos responsáveis por ele são:

- Ângelo Cabral - linkedin: https://www.linkedin.com/in/angelocassio/
- Felipe Chagas - linkedin:  
- Gabriela Nogueira - linkedin: https://www.linkedin.com/in/gabriela-nogueira/
- Vinicius Amorim - linkedin: https://www.linkedin.com/in/viniciusdeamorim/