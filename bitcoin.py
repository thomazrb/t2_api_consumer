import requests
from datetime import datetime

url = 'https://www.mercadobitcoin.net/api/ticker'

response = requests.get(url)

dados = response.json()

print(dados.get('ticker', None))
print(dados['ticker']['last'])

timestamp = dados['ticker']['date']
print('---')
print(datetime.fromtimestamp(timestamp).strftime('%a, %d-%m-%y %H:%M:%S'))