import requests
import json

response = requests.get("https://randomfox.ca/floof/")
print(response.status_code)
print(response.text)
print(response.content)
print(response.json())
print(json.loads(response.content))
