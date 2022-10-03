import requests

quotes = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
quotes_data = quotes.json()

for key, value in quotes_data.items():
    print('----------------------------')
    print(f'{key}')
    print('----------------------------')
    for key_intern, value_intern in value.items():
        print(f'{key_intern}: {value_intern}')

print('----------------------------')
