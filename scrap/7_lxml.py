from util import *
import lxml.html

html = download("http://example.webscraping.com/places/default/view/Afghanistan-1")

tree = lxml.html.fromstring(html)
td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]
area = td.text_content()
print area

"""
Downloading: http://example.webscraping.com/places/default/view/Afghanistan-1
647,500 square kilometres
"""