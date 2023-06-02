import os
import requests

os.system('cls||clear')

print("Converte um valor em dólar para real na cotação atual: ")

opcao = 1

while (opcao == 1): 
    
    usd_cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')

    usd = usd_cotacao.json()

    valorusd = usd['USDBRL']['high']

    real = float(input('Digite o valor em real: '))

    print(f'O valor de {real} convertido dolar é ${real * float(valorusd)}')
    
    opcao = int(input("Deseja verificar um novo valor?\nDigite: \n1 - SIM\n2 - NÃO\n"))
    
input("Aperte qualquer tecla para encerrar...")


