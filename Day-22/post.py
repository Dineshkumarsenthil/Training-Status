import requests

url = "308b23f91cb2dfee2dd934497a48e1d4"
file =  {"file" : open ("bob.txt" , '+rb')}
response  = requests.post(url,files=file)
print(response.status_code)
print(response.json())