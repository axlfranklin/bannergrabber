import requests

url = input("URL: ")
resposta = requests.get(url)

try:
    servidor = resposta.headers['Server']
    print(f'Server: {servidor}')
except KeyError:
    print('Erro!')
