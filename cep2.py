import requests


def exitable():
    option = input("Another consult CEP? (y)=yes: ")
    if option == 'y':
        return False
    return True


def main():
    print('-----------CEP-----------')

    cep_input = input("CEP: ")

    if len(cep_input) != 8:
        print('CEP is 8 digits!')
        exit() if exitable() else main()

    response = requests.get(f'https://viacep.com.br/ws/{cep_input}/json/')
    address_data = response.json()

    if 'erro' in address_data:
        print(f'{input()} is invalid!')
        exit() if exitable() else main()
    else:
        for key, value in address_data.items():
            print(f'{key}: {value}')
    exit() if exitable() else main()


if __name__ == '__main__':
    main()
