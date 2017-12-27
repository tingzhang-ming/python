from util import *

html = download("http://example.webscraping.com/places/default/view/Afghanistan-1")

print re.findall('<tr id="places_area__row">.*?<td\s*class=["\']w2p_fw["\']>(.*?)</td>', html)

"""
Downloading: http://example.webscraping.com/places/default/view/Afghanistan-1
['647,500 square kilometres']
"""