from bs4 import BeautifulSoup
import requests
import pynotify
#I imported beautifulsoup, urllib2 and pynotify in order to get the messgae to print to the terminal
#I defined the function to send the message with the message followed by the title so it looks like a notification one would get on their phone.
#To pull the quote out that I wanted, I used beautiful soup to extract the quote
#I was able to read the html file and pull the quote from the <div> class it was in
#I wrote out the author and specific message from the website so that it can print to the terminal as notification
def sendmessage(message, title):
    pynotify.init('Quotecatalog')
    notice = pynotify.Notification(message, title)
    notice.show()
    return Notification
URL = 'https://quotecatalog.com/quote/rupi-kaur-stay-strong-thr-baVPe57/'
r = requests.get(URL)
soup = BeautifulSoup(URL , 'html5lib')
print(soup.prettify())

author = 'Rupi Kaur'
title = author
message = 'stay strong through your pain, grow flowers from it!'
#defined the title and message from the website.
for words in soup.find_all('quotecatalog', 'class'):
    message.append(message.text.encode('content'))
    print(message)
#used a forloop to find the quote in the html file but it didn't do anything.
print(message, title)
#output quote followed by author's name!
