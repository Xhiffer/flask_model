import requests

num = 10
r = requests.post('http://localhost:5000/salaire.' + str(num))
print(r.json())