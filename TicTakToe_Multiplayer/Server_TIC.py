# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:33:48 2021

@author: siaaa013
"""


import socket
from _thread import *
import sys

server = "192.168.1.71"
port = 5050
ADDR = server, port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(ADDR)

s.listen(2)
print("Waiting for a connection, Server Started")


def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))
