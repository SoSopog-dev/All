import socket
import os



s = socket.socket()
host = socket.gethostname()
port = 5050
s.bind((host,port)) 
print ("The server is currently running", host)




s.listen(1)
conn, addr = s.accept()

print (addr, "Has connected to the network")

while 1:
    command = input()
