import requests

resp = requests.get(" https://jsonplaceholder.typicode.com/posts")
data = resp.json()
print(data)