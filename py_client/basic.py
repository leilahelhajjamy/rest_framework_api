import requests


#endpoint = "https://httpbin.org/status/200/"
endpoint = "http://127.0.0.1:8000/api/products/1/"



get_response = requests.get(endpoint , json = {"title": "my first post content"})
print(get_response.json())








