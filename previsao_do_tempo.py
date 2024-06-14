import requests

url = 'https://api.open-meteo.com/v1/forecast?latitude=-18.7197&longitude=-39.8586&current=temperature_2m&hourly=temperature_2m&daily=temperature_2m_max,temperature_2m_min&timezone=America%2FSao_Paulo&forecast_days=1'
response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(dados)
else:
    print('Erro consultando os dados')