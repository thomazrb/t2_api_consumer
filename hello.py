import requests

response = requests.get("https://www.google.com.br/")
dados_recebidos = response.text