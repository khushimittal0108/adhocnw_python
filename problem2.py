#!/usr/bin/python3
 
from googlesearch import search
import webbrowser

topic=input("Enter a topic to search :")
	
#for storing the urls create a list
search_list=[]
 
for i in search(topic,stop=10) :
	print(i)
	search_list.append(i) 
 
print("\n The list of url is = \n")
print(search_list)

#storing the url permanently
f=open('listurl.txt','a+')

for i in search_list :
	f.write(i+"\n")

