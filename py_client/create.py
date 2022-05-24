import requests

endpoint="http://localhost:8000/api/products/"


get_response = requests.post(endpoint , data= {"title":"hello beautiful laila , you ara a warrior , you can do it "})


print(get_response.json())