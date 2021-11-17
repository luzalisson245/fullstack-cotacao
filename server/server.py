import requests
api = '1b7f85ec8ad1184e690bd72f54828a40'
params = {'access_key': api, 'currencies': 'USD,EUR,CNY,HKD', 'format': 1}
r = requests.get('http://apilayer.net/api/live', params = params)
livequote = r.json()
print(livequote)