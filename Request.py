import requests
import bs4
requests.get
r = requests.get("https:.............")
type(r)
r.text
data = r.text
sakhtar = bs4.beautifulSoup(data)
sakhtar.select('title')