# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 14:29:06 2021

@author: siaaa013
"""


#main

import pygame
import numpy as mp
import math

import game



Width, Height = 900, 500

win = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Totaly War")

division_img = pygame.image.load("DIVISON.png")

FPS = 60

def draw_window():
    win.fill(255,255,255)
    pygame.display.update()

def main():
    
    clock = pygame.time.Clock()
    run = True 
    
    #main loop
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        
            
            
    pygame.quit()
    
    
if __name__ == "__main__":
    main()
    
        