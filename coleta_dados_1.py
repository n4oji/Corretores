import requests
import pandas as pd

base_url = "https://www.crecisc.conselho.net.br/form_pesquisa_cadastro_geral_site.php"

payload = {
    'acao': 'PesquisarCadastro',
    'OK': '1',
    'cidade': 'florianopolis'
}

response = requests.post(base_url, data=payload)

if response.status_code == 200:
  response_json = response.json() 

data = []
cadastros = response_json.get('cadastros', [])

for cadastro in cadastros:
  inscricao = cadastro.get('creci')
  identificacao = cadastro.get('nome')
  tipo_pessoa = 'PJ' if cadastro.get('tipo') == 2 else 'PF'
  situacao = 'ATIVO' if cadastro.get('situacao') == 1 else 'INATIVO'
  certidao_regularidade = 'APTO AO EXERCÍCIO' if cadastro.get('regular') == True else 'INDISPONÍVEL'
  contato = cadastro.get('telefones')
  if situacao == 'INATIVO':
    certidao_regularidade = 'INDISPONÍVEL'
  data.append([inscricao, identificacao, tipo_pessoa, situacao, certidao_regularidade, contato])

df = pd.DataFrame(data, columns=['inscricao', 'identificacao', 'tipo_pessoa', 'situacao', 'certidao_regularidade', 'contato'])
df.to_csv('corretores_florianopolis.csv', index=False)