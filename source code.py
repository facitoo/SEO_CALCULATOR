import tkinter as tk
from tkinter import *
import operator
from bs4 import BeautifulSoup
import requests
from PIL import Image , ImageTk
from urllib.request import urlopen
seo={}
string=''

#############################   web crawler   #########################

def spider (url):
    header=[]
    normal=[]
    txt=requests.get(url)
    content=txt.text
    soup=BeautifulSoup(content)
    for link in soup.findAll('h1'):
        t=str(link.string)
        sentence=t.lower().split()
        for word in sentence:
            header.append(word)
    for link in soup.findAll('h2'):
        t=str(link.string)
        sentence=t.lower().split()
        for word in sentence:
            header.append(word)
            
    for link in soup.findAll('p'):
        t=str(link.string)
        sentence=t.lower().split()
        for word in sentence:
            normal.append(word)
    filtr(header,normal)
		
##############################   online content extractor   ###################

def spider2 (url):
    header=[]
    normal=[]
    txt=requests.get(url)
    content=txt.text
    soup=BeautifulSoup(content)
    for link in soup.findAll('a'):
        t=str(link.string)
        sentence=t.lower().split()
        for word in sentence:
            normal.append(word)
    filtr(header,normal)
        

##############################   filter for words   ##############################    
    
def filtr (head,norml):
    header=[]
    normal=[]
    conectors=['is','am','are','the','and','or','for','who','by','a','that','about','com',
    'with','he','too','she','it','they','on','at','then','may','able','us','what','be'
    ,'sholud','done','all','you','i','why','how','an','them','am','so','for','j','b','c','d','e','f'
    ,'g' ,'next','also','like','since','because','hi','thats','me','due','whenever','none','h','i','k'
    ,'since','unless','infact','unlike','still','hence','yet','besides','just','even','have','your','l'
    ,'my','be''there','of','in','as','make','we','of','to','m','n']    #restrected words to be removed
    symbols="!@#$%^&*()_+{}|:\"<>?1234567890-=[]\;',.©/`~"           #string for special symbol
    for word in norml:
        for i in range(0,len(symbols)):
            word=word.replace(symbols[i],'')
        if len(word)>0:
            for i in range(len(conectors)):  #checking for conectors
                if word == conectors[i]:    
                    word=''
            if len(word)>0:                  #checking for woeds with only special symbol
                normal.append(word)
    for word in head:
        for i in range(0,len(symbols)):
            word=word.replace(symbols[i],'')    #replace function defined in oprator library
        if len(word)>0:
            for i in range(len(conectors)):
                if word == conectors[i]:
                    word=''                  #replacing with enpty string
            if len(word)>0:
                header.append(word)
    Seo(header,normal)                       #calling Seo function
    
##########################   Seo function   #########################    
    
def Seo (header,normal):
    i=0
    for word in header:
        seo[word]=10
        
    for word in normal:
        if word in seo:
            seo[word]+=1
        else:
            seo[word]=1
    root=tk.Tk()
    root.title('results')
    lbl=Label(root,text="The COntent Of Web Site is...")
    #root.geometry('600x600')  #geometry not included as panel uses grid layout
    x=[]  
    for key, value in sorted(seo.items(), key=operator.itemgetter(1)): #filter for small words
        if value != '1' or value !='2':
            x.append(key)
    if len(header) == 0:	
    	y=x
    else:
	y=x[::-1]
    print(y) #check function ### to be removed###
    for i in range(len(y)):
        Label(root, text = y[i]).grid(row=i,ipadx = 10,ipady = 50)
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox = Listbox(root, yscrollcommand=scrollbar.set)
    text = Text(root)
    for i in range(1000):
        listbox.insert(END, str(i))
    for line in range(0,i):
        mylist.insert(END)
    text.insert(END, "ansjfnafjasf")
    text.pack()
    listbox.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command = listbox.yview)
    lbl.pack()
    mainloop()  # running the nwe aplet window
        
#################################   application main body   #########################

app=tk.Tk()
app.configure(background='white')
newImageSizeWidth=100
newImageSizeHeight=100
app.title("Search")
def on_button():       #on button geting the string entered in the text field
    string=entry.get()
    if string=='':   #exception NULL IN STRING handeled
        return
    print(string)
    spider(string)  #calling main web crawler
def clear_text():
        entry.delete(0, 'end')
def content():
    string=entry.get()
    print(string )
    spider2(string)
app.geometry('300x200')  #size of main window
same = True
n=.25

path =r'C:\Users\Abhi\Desktop\photo.jpg'
image = Image.open(path)
[imageSizeWidth, imageSizeHeight] = image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 

 image = image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)

Canvas1 = Canvas(app)
Canvas1.create_image(newImageSizeWidth/2,newImageSizeHeight/2,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(side=TOP,expand=True)
labl=Label(app,text="Facitoo Search",bg="white",fg="black")
button = tk.Button(app, text="SEO", command=on_button)          #event handling for geting the text
button3 = tk.Button(app, text="Get Content", command=content)
button2 = tk.Button(app, text="clear", command=clear_text)      #event for clearing the textbox
entry = tk.Entry(app)
labl.pack()
entry.pack()
button.pack(padx=20, pady=10, side=LEFT)
button3.pack(padx=20, pady=20, side=LEFT)
button2.pack(padx=20, pady=20, side=LEFT)
app.mainloop()
