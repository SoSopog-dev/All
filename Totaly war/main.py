# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 09:25:11 2021

@author: siaaa013
"""


import pygame

import game


sprites = []

Width, Height = 900, 500

win = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Totaly War")

division_img = pygame.image.load("DIVISION.png")
bg = pygame.image.load("bg.png")
pygame.init()

FPS = 60

def main():
    clock = pygame.time.Clock()
    run = True 
    down_press = False
    #main loop
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        
    pygame.quit()