from util import *
from bs4 import BeautifulSoup

html = download("http://example.webscraping.com/places/default/view/Afghanistan-1")
soup = BeautifulSoup(html)
tr = soup.find(attrs={'id':'places_area__row'})
td = tr.find(attrs={'class':'w2p_fw'})
print td.text


"""
647,500 square kilometres
"""