#!/usr/bin/python3

import os
#imported crypt for encrypting the password
import crypt 

name=input("Enter a user name :")

#name.isalpha() will check is the srting consist of only alphabets
if name.isalpha() :
	password="hello"+name
	encryptpass=crypt.crypt(password,"aa")
	#this is used to provide encrypted password beginning with aa
	os.system("useradd -p"+encryptpass+" "+name)
	#this is used to run command in terminal for adding user and setting its password
	print("User has been created")
else :
	print("Invalid username, it should only contain alphabets")
