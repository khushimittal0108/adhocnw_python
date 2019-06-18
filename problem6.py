#!/usr/bin/python3

print("----OPTIONS---- \n 1.cat file \n 2.cat >file \n 3.cat file >file2 \n 4.cat file >>file2")
print("Enter your choice :")
choice=int(input())

#Display the contents of file 
if choice == 1 :
	f=open('file.txt','r')
	content=f.read()
	print(content)
	f.close()

#Create an empty file and enter data into it
elif choice == 2 :
	f=open('file.txt','w')
	print("Enter data into file (to exit type E) :")
	data=input()
	while data != 'E' :
		f.write(data+"\n")
		data=input()
	f.close()

#copy the contents of one file to file2 and display the contents of file2
elif choice == 3 :
	f=open('file.txt','r')
	open('file2.txt','w').close()
	f2=open('file2.txt','r+')
	for line in f :
		f2.write(line)
	print("the content of file2 :")
	f2.seek(0)
	content=f2.read()
	print(content)
	f2.close()
	f.close()

#append the contents of file at the end of file2 and display the contents of file2
elif choice == 4 :
	f=open('file.txt','r')
	f2=open('file2.txt','a+')
	for line in f :
		f2.write(line)
	print("the content of file2 :")
	f2.seek(0)
	content=f2.read()
	print(content)
	f2.close()
	f.close()
else :
	print("Invalid choice")
	
