import requests
from bs4 import BeautifulSoup
import pynotify
from time import sleep
def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification('Rupi Kaur' , 'Stay strong!')
    notice.show()
    return
url = "https://quotecatalog.com/quote/rupi-kaur-stay-strong-thr-baVPe57/"
while True:
    r = requests.get(url)
    while r.status_code is not 200:
            r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')
    data = soup.find_all("quotecatalog")
