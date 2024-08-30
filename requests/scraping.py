import requests;

response = requests.get('https://www.wikipedia.org/')

print('Status code:', response.status_code)
print('Header:')
print(response.headers)
print('Content:')
print(response.content)