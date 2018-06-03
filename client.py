import requests
import json

data = {
    'ja' : 'こんにちは',
    'other' : 'Hello.'
}

header = {
    'Content-Type':'application/json'
}

print(json.dumps(data))

r = requests.post(
    'http://localhost:8080/pair/update/status',
    data=json.dumps(data),
    headers=header
)

print(r)
