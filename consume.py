#a request to python to consuming the api through the frontent
#need to import request (install requests) - module to make simple requests to pages on the internet 


import requests

response = requests.get('http://127.0.0.1:8000/pokemart_list')
print(response.json())

