#!/usr/bin/python2

import socket
import sys

local_ip="127.0.0.1"
local_port=4545
time=100
#you can assign any free port ,to see used udp ports use netstat -nulp

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.settimeout(time)
while 5>2 :
	message=raw_input("Sender :")
	s.sendto(message,(local_ip,local_port))
	t=s.recvfrom(150)
	if len(t[0]) == 150 :
		print("Cannot recieve Very long Text")
	print("Reply from Reciever:" +t[0])
	ques=raw_input("Do you want to quit the conversation (Y/N) :")
	#if the Sender want to quit then type Y
	if ques == 'Y' :
		s.sendto("Exited",(local_ip,local_port))
		exit()
