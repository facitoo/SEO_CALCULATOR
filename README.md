# SEO_CALCULATOR
this project is all about web crawling and basic python GUI 
lib used:
  1. tkinter (GUI LIB)
  2. requests (networking)
  3. bs4 (for reading the HTML doc )
  4. PIL (python image lib)
  5. opetrator (basic string functions)
  6. urllib (accesing ofline HTML doc/online)
functions used:
  1. spider/spider2 (web cralwers and 'spider' looks classy)
  2. filtr (for  filtering the data colecteed)
  3. SEO (for counting the occurance of letters(always use this after filter as it will reduce both time and memory complexcity)
 main body:
  the main body contains a tkinter window (GUI) wit a text field and three buttons. the input is in form of url which is to be 
  crawled and the input is thn sent to spider/spider2 function for furter process. the get content button returnd the top 5 top
  content of the web site both online or ofline HTML doc.
