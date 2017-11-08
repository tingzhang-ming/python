from PySide.QtWebKit import *
from PySide.QtCore import *
from PySide.QtGui import *
import lxml.html

url = "http://example.webscraping.com/places/default/search"

app = QApplication([])
webview = QWebView()
loop = QEventLoop()
webview.loadFinished.connect(loop.quit)
webview.load(QUrl(url))
loop.exec_()
webview.show()
frame = webview.page().mainFrame()

frame.findFirstElement('#search_term').setAttribute('value', '.')
frame.findFirstElement('#page_size option:checked').setPlainText('1000')
frame.findFirstElement('#search').evaluateJavaScript('this.click()')
app.exec_()