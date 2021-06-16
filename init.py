# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 08:27:15 2021

@author: siaaa013
"""
import os

#__init__



#os.system("pip install --user pyautogui")

#os.system("pip install --user keyboard")

import subprocess

#proc = subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE, shell=True)
#(out, err) = proc.communicate()

#print ("program output:", out)

commands = """netstat
              echo hello | wc -l
              ps aux | grep python"""
b = subprocess.check_output(commands, shell=True)
print(b.decode('ascii'))

#os.system("first command\nsecond command\nthird command")














































