
artist_name = input()

URL = "https://altwall.net/texts.php?show=" + artist_name

import requests

r = requests.get(URL)
r.encoding = r.apparent_encoding
raw_artist_page = r.text

from bs4 import BeautifulSoup

page_soup = BeautifulSoup(raw_artist_page, 'html.parser')

print(page_soup.prettify())

songs_url = []
