#!/usr/bin/python3
import socket

def sender(ip,port,count):
    re_ip=ip
    re_port=port

    # creating socket
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    s.sendto(count,(re_ip,re_port))
    return True 


