#!/usr/bin/python3
# This liberary is used to create and manage network sockets using Python
import socket

# The function sender uses the ip and port as parameter
def sender(ip,port,count):
    # This is used to assign Ip adderess to the variable
    re_ip=ip
    # This is used to assign the port to the variable
    re_port=port

    # creating udp socket
    # SOCK_DGRAM is used to specify that this socket is a UDP socket
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    # This function is used to send the count with the ip and port
    s.sendto(count,(re_ip,re_port))
    # Now returning true for execution
    return True 


