# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 11:56:34 2021

@author: siaaa013
"""


#Tick Tack Toe

import pygame
import numpy as np

board = [[0,0,0],[0,0,0],[0,0,0]]

Width, Height = 189, 189

win = pygame.display.set_mode((Width, Height))

pygame.display.set_caption("Tick Tack toe")
cross_img = pygame.image.load("COROSS.png")
circle_img = pygame.image.load("CIRCILE.png")
bg = pygame.image.load("BG.png")


pygame.init()
class squeras(object):
    def __init__(self, x, y, h, w, number, row):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.absolute_type = 190
        
        self.selected = False
        self.number = number
        self.row = row
        self.rect = pygame.Rect(x,y,w,h)
        
    def selecting(self, type):
        point = pygame.mouse.get_pos()
        if pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(point) == True and self.selected == False:
                self.selected = True
                self.type = type    
                return True

     
    def draw(self, win, cross_img, circle_img):
        if self.selected == True:
                
            if self.type == 1:
                win.blit(circle_img, (self.x -1,  self.y -1))
            if self.type == -1:
                win.blit(cross_img, (self.x -1, self.y -1))
   
def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0

def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return 0

def checkWin(board):
    #transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)
    
    
def redraw_win(win, sprites):
    for i in sprites:
        i.draw(win, cross_img, circle_img)
        pygame.display.update()
    
win.blit(bg,(0,0))      
 
def main():
    clock = pygame.time.Clock()
    FPS = 60
    run = True 
    down_press = False
    turn = 1
    
    squeras0 = squeras(0,0,60,60,0,0)
    squeras1 = squeras(65,0,60,60,1,0)
    squeras2 = squeras(130,0,60,60,2,0)
    
    squeras3 = squeras(0,65,60,60,3,1)
    squeras4 = squeras(65,65,60,60,4,1)
    squeras5 = squeras(130,65,60,60,5,1)
    
    squeras6 = squeras(0,130,60,60,6,2)
    squeras7 = squeras(65,130,60,60,7,2)
    squeras8 = squeras(130,130,60,60,8,2)
    
    sprites = [squeras0,squeras1,squeras2,squeras3,squeras4,squeras5,squeras6,squeras7,squeras8,]
    
    while run:
        output = 0
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if down_press == False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                down_press = True
                for s in sprites:
                    answer = s.selecting(turn)
                    if answer == True:
                        print(turn)
                        number = s.number%3
                        print(number)
                        board[s.row][number] = turn
                        print(board)
                        turn = turn * -1
                        break
                        
        if event.type == pygame.MOUSEBUTTONUP:
            down_press = False
        for i in range(3):
            if 0 in board[i]:
                output = 1
        if output == 0:
            run = False
            
                
            
        if checkWin(board) == 1 or checkWin(board) == -1:
            run = False
        redraw_win(win, sprites)
                             
                    
        
    pygame.quit()
        
if __name__ == "__main__":
    main()
        



        