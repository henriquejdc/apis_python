import requests


def login(email, password):
    session = requests.Session()
    paylod = {
        'email': email,
        'password': password
    }
    response = session.post('https://api.giggl.app/v1/auth', json=paylod)
    print(response.json())
    if 'error' not in response.json():
        session.headers.update({'authorization': response.json()['token']})
    print(response.content)
    return session


session = login('email', 'pass')
response = session.patch('https://api.giggl.app/v1/users/@me', json={'location': 'Brazil'})
print(response.content)
