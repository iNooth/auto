
import requests


alvo = 'colar site aqui'

listas = ["admin", " Painel", "css", "php"]
r = requests.get(alvo)

for listas in listas:
  
  print(alvo + listas)

