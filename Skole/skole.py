# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 09:12:58 2021

@author: siaaa013
"""
import math



def vol_cyl(r, h):
    pi = math.pi
    Volume = pi*r*r*h
    print (Volume)
    return Volume

def vol_shere(r):
    pi = math.pi
    Volume = (4*r*r*r*pi)/3
    print(Volume)
    return Volume

def main():
    request = input("Hvilken form vil du regne ut volumet til: Cir eller Syl ")
    
    if request == "Cir":
        try:
            r = int(input("Hva er radien til kulen din"))
            Volume = vol_shere(r)
        except:
            print("Dette er ikke et gyldig tall")
    elif request == "Syl":
        try:
            r = int(input("Hva er radien til sylinderen din"))
            h = int(input("Hva er høyden til sylinderen din"))
            Volume = vol_cyl(r,h)
            
        except:
            print("Et av disse tallene er ikke et gyldig tall")
    else:
        print("Dette er ikke en av valgene")
        
            
