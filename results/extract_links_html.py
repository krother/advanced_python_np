"""
Download a Wikipedia page and save all hyperlinks
to a CSV file

preparations:

    pip install httpx bs4 pandas
"""
from pprint import pprint

import httpx  # library for downloading web pages
import bs4    # library for parsing HTML
import pandas as pd
# ! do not use requests, it is more or less obsolete !

# download page
url = "https://en.wikipedia.org/wiki/Timi%C8%99oara"
page = httpx.get(url)
print(page.status_code)
print(page.text[:100])
print(len(page.text))
open("timisoara.html", "w").write(page.text)

# parse HTML
# 3 choices to parse HTML: scrapy, re, BeautifulSoup
soup = bs4.BeautifulSoup(page.text, "lxml")
links = list(soup.find_all("a"))
print(len(links))

data = [(lk.text, lk.get("href", "-")) for lk in links]
pprint(data[:5])

# write to file
df = pd.DataFrame(data, columns=["label", "href"])
df.to_csv("links.csv")
