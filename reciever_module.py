#!/usr/bin/python3
import socket

def reciever(ip,port):
    re_ip=ip
    re_port=port  # fixed with us 

    # creating udp socket
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # Binding ip and port
    s.bind((re_ip,re_port))
    # code to recieve data
    data=s.recvfrom(1000)
    data = data[0]
    return data
    
