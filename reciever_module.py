#!/usr/bin/python3
# This liberary is used to create and manage network sockets using Python
import socket

# The function reciever uses the ip and port as parameter
def reciever(ip,port):
    # This is used to assign Ip adderess to the variable
    re_ip=ip
    # This is used to assign the port to the variable
    re_port=port  # fixed with us 

    # creating udp socket
    # SOCK_DGRAM is used to specify that this socket is a UDP socket
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # Binding ip and port in the socket
    s.bind((re_ip,re_port))

    # The recvfrom function is used to start listening to the system and
    # The parameter in this funtion represents the number of characters it can recieve
    data=s.recvfrom(1000)
    # Now we are using the first value of data since the data is a list and we need the 1st value of it
    data = data[0]
    # Now we are sending the recieved data
    return data
    
