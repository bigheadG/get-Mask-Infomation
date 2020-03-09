import csv
import requests
url = "https://data.nhi.gov.tw/resource/mask/maskdata.csv"
with requests.Session() as s:
    cr = csv.reader(s.get(url).content.decode('utf-8').splitlines(), delimiter=',')
    [print(row) for row in list(cr)]

