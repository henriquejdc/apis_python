import requests

URL = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking'


def exitable():
    option = input("Another consult? (y)=yes: ")
    if option == 'y':
        return False
    return True


def main():
    print('-----------Name Ranking Decade IBGE Chapecó or SC or BR -----------')

    params = {
        'decada': input("Decade: Ex: 1950 ")
    }

    state = input("C - Chapecó | SC | BR: ")

    if state == 'C':
        state = 4204202
    elif state == 'SC':
        state = 42

    params['localidade'] = state

    sex = input("Sex? M - Male | F - Female | N - No: ")

    if sex in ['M', 'F']:
        params['sexo'] = sex

    response = requests.get(URL, params=params)
    ranking_data = response.json()

    if 'erro' in ranking_data:
        print(f'{input()} is invalid!')
        exit() if exitable() else main()
    else:
        for data in ranking_data:
            for key, value in data.items():
                if key != 'res':
                    print(f'{key}: {value}')
                else:
                    for r in value:
                        print(r)
    exit() if exitable() else main()


if __name__ == '__main__':
    main()
