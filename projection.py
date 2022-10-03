import requests


URL = 'https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/'


def exitable():
    option = input("Another consult? (y)=yes: ")
    if option == 'y':
        return False
    return True


def main():
    print('-----------Projection IBGE 0-5 Regions or BR -----------')

    state = input("0-5 Regions or BR: ")

    response = requests.get(URL+str(state))
    projection_data = response.json()

    if 'erro' in projection_data:
        print(f'{input()} is invalid!')
        exit() if exitable() else main()
    else:
        for key, value in projection_data.items():
            if key != 'projecao':
                print(f'{key}: {value}')
            else:
                for key, value in value.items():
                    print(f'{key}: {value}')
    exit() if exitable() else main()


if __name__ == '__main__':
    main()
