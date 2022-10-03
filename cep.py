import requests
import os

cep = input("CEP: ")
response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
json = response.json()

if response.status_code == 200:
    print('Ok')
else:
    print('Error')

list(json)           # ['a', 'b', 'c']             the keys
list(json.keys())    # ['a', 'b', 'c']             the keys
list(json.values())  # [1, 2, 3]                   the values
list(json.items())   # [('a',1), ('b',2), ('c',3)] a tuple of (key, value)
print(json.items())  # dict_items([...)

for key, value in json.items():
    print(f'{key}: {value}')
