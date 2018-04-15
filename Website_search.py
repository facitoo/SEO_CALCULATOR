# --------------------- Facitoo ------------------------ #
# just a basic python code (need to be modified for further use) if you are using this the input will be from the terminal/cmd #

import requests
from bs4 import BeautifulSoup

###################### search function ####################

def spider(url,search_key):            #parameters as url of the web site and search item
	flag=0                            
	conection=requests.get(url)          # establishing conection
	txt=conection.text                   #converting into text
	soup=BeautifulSoup(txt)
	print("search results:")
	for link in soup.findAll('a'):
		title=link.string
		if title == search_key:
			print("found :" + search_key)    
			hef=url+str(link.get('href'))      #extracting link to the searched keyword
			print("domain is: "+hef)
			flag=1            
	if flag == 0:
		print("Nothing Found with "+search_key+" try using another word!")

############################ main body ###################

url=str(input("enter url: "))                            # input of the website to be searched for the keyword
key=str(input("what you want to search on this domain")) # input of the search key

spider(url,key) 
