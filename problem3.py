#!/usr/bin/python3

adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]

l1=[]
l2=[]
#part i print numbers greater than 5
print("Numbers > 5:")
for i in adhoc :
	if i > 5 :
		print(i)
		l1.append(i)

#part ii print numbers less than or equals to 2
print("Numbers <= 2:")
for i in adhoc :
	if i <= 2 :
		print(i)
		l2.append(i)

#part iii
#alternate method for directly storing in list
#storing number greater than 5 in list1
#l1=[for i in adhoc if i > 5]
#storing number less than or equals to in list2
#l2=[for i in adhoc if i <= 2]

print("Numbers greater than 5 ,list1 =",l1)
print("Numbers less than or equals to 2 ,list2=",l2)

