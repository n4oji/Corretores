# Coleta de Dados de Corretores de Imóveis - Florianópolis

## Descrição do Projeto

Este projeto tem como objetivo coletar dados de corretores de imóveis cadastrados no site do CRECI-SC, filtrando pela cidade de Florianópolis. A coleta de dados é realizada através de uma requisição à API do site, que retorna as informações necessárias. Os dados são então processados e armazenados em um arquivo CSV.

## Pré-requisitos

- Python 3.x
- Bibliotecas `requests` e `pandas`

## Instalação

1. Clone o repositório para sua máquina local:

    ```bash
    git clone https://github.com/n4oji/Corretores.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd Corretores
    ```

3. Instale as bibliotecas necessárias:

    ```bash
    pip install requests pandas
    ```

## Uso

Para executar o script e coletar os dados, siga os passos abaixo:

1. Execute o script `coleta_corretores.py`:

    ```bash
    python coleta_corretores.py
    ```

2. O script enviará uma solicitação POST para a API do CRECI-SC e processará a resposta, extraindo os dados dos corretores.

3. Os dados coletados serão armazenados em um arquivo CSV chamado `corretores_florianopolis.csv` no mesmo diretório do script.

## Detalhamento do Script

O script `coleta_corretores.py` realiza as seguintes etapas:

Dentro do diretório Resultados estão o csv com o Dataframe que eu montei e o json que a API me retornou dos corretores de Florianóplois.

## Limitações

### Exercício 2: Coleta de Dados - Corretores SP - São Paulo (Apenas Ativos)

Infelizmente, não foi possível concluir o segundo exercício de coleta de dados dos corretores de imóveis cadastrados no site do CRECI-SP para a cidade de São Paulo. O site utiliza o sistema reCAPTCHA, que impede a automação de consultas por scripts. 

O reCAPTCHA é uma medida de segurança que visa proteger o site contra acessos automatizados e bots, o que torna inviável a realização de scraping diretamente através de código.

Como alternativa, uma possível solução seria utilizar técnicas de reconhecimento e resolução de reCAPTCHA, mas isso exige ferramentas avançadas e pode infringir os termos de serviço do site, além de ser eticamente questionável.

Agradecemos a compreensão.