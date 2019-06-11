#!/usr/bin/python3

import datetime

#take input from user
name=input("Enter your name:")
age=int(input("Enter your age (You are/will turn this year):"))

cur_year=datetime.datetime.now().year

#calculating the year when user will turn 95
year=cur_year+95-age

print("The year you will turn 95 is : ")
print(year)
