# consuming the api through the frontent
#need help with this

import requests

response = requests.get('http://127.0.0.1:8000/pokemart_list')
print(response.json())

