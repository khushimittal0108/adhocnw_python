#!/usr/bin/python2

import socket

recv_ip="127.0.0.1"
recv_port=4545
#you can assign any free port ,to see used udp ports use netstat -nulp

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#use these for ip type v4 and udp 

#fitting ip and port with udp socket
#remember ip address + port = socket
s.bind((recv_ip,recv_port))

while 7>5 :
	r=s.recvfrom(150)
	if len(r[0]) == 150 :
		print("Can't Recieve very long text")
	print("Sender:" +r[0]) 
	if r[0] == 'Exited':
		exit()
	reply=raw_input("Enter your Reply:")
	client_address=r[1]
	s.sendto(reply,client_address)

