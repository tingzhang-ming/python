from PySide.QtWebKit import *
from PySide.QtCore import *
from PySide.QtGui import *
import lxml.html

url = "http://example.webscraping.com/places/default/dynamic"

app = QApplication([])
webview = QWebView()
loop = QEventLoop()
webview.loadFinished.connect(loop.quit)
webview.load(QUrl(url))
loop.exec_()
html = webview.page().mainFrame().toHtml()

tree = lxml.html.fromstring(html)
print tree.cssselect('#result')[0].text_content()

"""
Hello World
"""