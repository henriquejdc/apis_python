import requests

response = requests.get('https://xkcd.com/353/comics/python.png')

if response.ok:  # already
    with open('comic.png', 'wb') as f:
        f.write(response.content)

payload = {'page': 2, 'count': 25}
# response = requests.get('https://httpbin.org/get?page=2&count-25')
response_get = requests.get('https://httpbin.org/get', params=payload)
print(response_get.json())

data = {'username': 'henrique', 'password': 'teste'}
response_post = requests.post('https://httpbin.org/post', data=data)
print(response_post.json()['form'])

auth = ('henrique', 'teste')
response_get_auth = requests.get('https://httpbin.org/basic-auth/henrique/teste', auth=auth)
print(response_get_auth.json())


response_get_delay = requests.get('https://httpbin.org/delay/2', timeout=3)  # timeout 3s
print(response_get_delay.json())
