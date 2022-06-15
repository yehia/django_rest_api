import requests

endpoint = 'http://127.0.0.1:8000/api/'


get_response = requests.post(endpoint, json={'title': 'Abc123', 'content': 'Hellow World'})
# print(get_response.headers)
# print(get_response.text)
# print(get_response.status_code)

print(get_response.json())