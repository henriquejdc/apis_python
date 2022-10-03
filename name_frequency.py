import requests

URL = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/'


def exitable():
    option = input("Another consult? (y)=yes: ")
    if option == 'y':
        return False
    return True


def main():
    print('-----------Frequency Name IBGE Chapecó or SC -----------')

    name_input = input("Name: ")
    state = input("C - Chapecó | SC | BR: ")

    if state == 'C':
        state = 4204202
    elif state == 'SC':
        state = 42

    params = {
        'localidade': state
    }

    sex = input("Sex? M - Male | F - Female | N - No: ")

    if sex in ['M', 'F']:
        params['sexo'] = sex

    response = requests.get(URL+name_input, params=params)
    frequency_data = response.json()

    if 'erro' in frequency_data:
        print(f'{input()} is invalid!')
        exit() if exitable() else main()
    else:
        for data in frequency_data:
            for key, value in data.items():
                if key != 'res':
                    print(f'{key}: {value}')
                else:
                    for r in value:
                        print(r)
    exit() if exitable() else main()


if __name__ == '__main__':
    main()
