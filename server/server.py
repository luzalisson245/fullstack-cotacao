import requests
from pymongo import MongoClient

api = '1b7f85ec8ad1184e690bd72f54828a40'
params = {'access_key': api, 'currencies': 'USD,EUR,CNY,HKD', 'format': 1}
r = requests.get('http://apilayer.net/api/live', params = params)
livequote = r.json()
print(livequote)

client = MongoClient("mongodb+srv://luzalisson245:wlmbuthn@cluster0.ew4ps.mongodb.net/Cluster0?retryWrites=true&w=majority")
db = client.test
db.createCollection("colecao1")