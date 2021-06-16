# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 08:55:08 2021

@author: siaaa013
"""
#alphabet
a = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
#gets the lenth of the alphabet
l = len(a)

#function encode
def encode(message, key):
    output = ""
    #goes though every eltter in the message
    for letter in message:
        #Cechs if letter in the aphabet
        if letter in a:
            #if it is in alphabet find the position of the letter
            pos = a.find(letter)
            #new_pos is the position - the key then modulo to make
            new_pos = (pos + key) % l
            #adds the new letter to output
            output = output + a[new_pos]
        else:
            #if the letter is not in althabet add it to output
            output = output + letter
    return output
    
#function decode
def decode(message, key):
    output = ""
    #goes though every letter in the message
    for letter in message:
        #Chechs if letter is in alphabet
        if letter in a:
            #if it is in alphabet find the position of the letter
            pos = a.find(letter)
            #new_pos is the position - the key then modulo to make
            new_pos = (pos - key) % l
            if new_pos <= 0:
                new_pos += l
            output = output + a[new_pos]
        else:
            output = output + letter
    return output
    
#funtionc bruteforce
#this function just shows all of the versions of the message decoded to every key possible
def bruteforse(message):
    output = []
    for i in range(l):
        output.append(" ")
                   
    for number in range(l):
        output[number- 1] = decode(message,number) + str(number)
    return output
        
#main loop
run = True
while run:
    #asks whitch mode the user wants it to be in
    answer = input("\n Do you want to encode or decode or bruteforce>>> e/d/b ")
    #e encodes the message
    if answer ==  "e":
        message = input("\n Encode your message>>>")
        try:
            key = int(input("\n What is the key>>>"))
        except:
            print("Not a valid number")
        message = encode(message,key)
        print(message)
    #d decodes the message    
    elif answer == "d":
        message = input("\n Decode your message>>>")
        try:
            key = int(input("\n What is the key>>>"))
        except:
            print("\n Not a valid number")
        message = decode(message,key)
        print(message)
    #b bruteforcec the message
    elif answer == "b":
        message = input("\n Bruteforce your message>>>")
        answer = bruteforse(message)
        print(answer)
    #k kills the program
    elif answer == "k":
        run = False
    else:
        print("anwer not valid")

    
    