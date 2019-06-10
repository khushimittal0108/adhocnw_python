#!usr/bin/python3

import datetime

name=input("Enter your name :")

#for optimization store datetime.datetime.now() in variable say now
now=datetime.datetime.now()

#now.hour will show the hour from the function datetime.datetime.now()
#If else for appropriate greeting

if now.hour > 6 and  now.hour < 12:
	print("Good morning !!" , name)
elif now.hour > 12 and  now.hour < 16:
	print("Good Afternoon !!" , name)
elif now.hour > 16 and  now.hour < 20:
	print("Good Evening !!" , name)
elif now.hour > 20 and  now.hour < 6:
	print("Good night !!" ,name)
