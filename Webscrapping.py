import requests
from fake_useragent import UserAgent
url=("https://books.toscrape.com/")
r  = requests.get(url)
with open("file2.html","w") as f:
    f.write(r.text)