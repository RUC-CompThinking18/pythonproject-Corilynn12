#I have to scrape the quotes from a website in order to print them to the terminal. I then have to find a way to send that specific
#quote as a notification to the terminal. I have to beautifulsoup, requests,and html5lib in order to extract the quotes I need from the website.
#I also need to import beautiful soup and request that it extracts the data needed from the website
import requests
from bs4 import BeautifulSoup
import csv
URL = "https://www.goodreads.com/author/quotes/8075577.Rupi_Kaur"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())
quotes=[]
table = soup.find('div', attrs = {'class' : 'quote'})
file_name = 'Rupi_Kaur_quotes.csv'
with open(file_name, 'wb') as f:
    w = csv.DictWriter(f,['url' , 'author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
