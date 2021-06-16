import socket
import os

s = socket.socket()
host = input()
port = 5050

s.connect((host,port))


while 1:
    
