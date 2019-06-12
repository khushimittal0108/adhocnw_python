#!/usr/bin/python3

import datetime

name=input("Enter your name:")
age=int(input("Enter your age:"))
print("enter your dob:")
dd=int(input("Enter date:"))
mm=int(input("Enter month:"))
yyyy=input("Enter year:")

d=datetime.datetime.now()
cur_year=d.year

#use d.strftime() to print date and month as it returns string and use type conversion
#To calculate the correct year we check this condition - birthday -already gone or coming
if int(d.strftime("%m")) > mm :
		year=cur_year+95-age
elif int(d.strftime("%m")) == mm :
	if int(d.strftime("%d")) >= dd :
		year=cur_year+95-age
else :
	year=cur_year+95-age-1

print("The year you will turn 95 is : ")
print(year)
