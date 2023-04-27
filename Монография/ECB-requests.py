import requests
import pandas as pd

series_key2 = 'EXR/D.CHF.EUR.SP00.A'

url = 'https://sdw-wsrest.ecb.europa.eu/service/data/'
# headers used as content negotiation to return data in json format
headers = {'Accept':'application/json'}
r = requests.get(f'{url}{series_key2}', headers=headers).json()

print(r['dataSets'][0])