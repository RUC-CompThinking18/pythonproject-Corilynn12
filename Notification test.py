import requests
from bs4 import BeautifulSoup
import pynotify
from time import sleep
message = "Stay strong, it takes grace to remain kind in cruel situations."
def sendmessage(title, message):
    pynotify.init('https://quotecatalog.com/quote/rupi-kaur-stay-strong-thr-baVPe57/')
    notice = pynotify.Notification('title' , 'message')
    notice.show()
    return Notification
print(message)
