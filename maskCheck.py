import csv
import requests as s
url = "https://data.nhi.gov.tw/resource/mask/maskdata.csv"

cr = csv.reader(s.Session().get(url).content.decode('utf-8').splitlines(), delimiter=',')
[print(row) for row in list(cr)]



'''
import csv
import requests
with requests.Session() as s:
	cr = csv.reader(s.get(url).content.decode('utf-8').splitlines(), delimiter=',')
	[print(row) for row in list(cr)]
'''
