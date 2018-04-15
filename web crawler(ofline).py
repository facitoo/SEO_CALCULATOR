# --------------------------------------- Facitoo ---------------------------#
# this is how to crawl a ofline web page saved locally #

from urllib.request import urlopen
from bs4 import BeautifulSoup
import downlodr

################################ web crawler ##################################

def spider(number):                                       #function for crwaling with parameter of number of pages
	num=1
	while num<=number:
		url='file:///home/facitoo/Desktop/main_page.html'     # path to ofline saved HTML page
		status=urlopen(url)                                   # opening the HTML doc
		text=status.read()
		soup=BeautifulSoup(text)                
		for link in soup.findAll('button',{'type':'submit'}):   
			title=link.string
			ref=link.get('href')                                #geting hyperlinks 
			print(title)
			print(ref)
			print('1')
		num+=1
    
spider(1)                 #passing number of pages to be crawled (by default = 1)
