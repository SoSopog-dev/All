"""Totaly war"""

import pygame
from pygame.constants import K_x

#this is a class for a pair of a pointer and a division
class pair_d_p():
    def __init__(self,):
        self.number = 1
        self.type = "good"
    #this is the player divisions
    class div():
        def __init__(self,x,y,w,h):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.Rect = pygame.Rect(self.x, self.y, self.w, self.h)
        def draw(self,win):
            
        
    #this is the pointer class
    #it indicates where the division is going to go
    class point():
        def __init__(self,x, y):
            self.x = x
            self.y = y
            self.show = False
        def draw(self, win):
            if self.show == True:
                win.blit(self.img,(self.x,self.y))

            
#this is a class for the enemy divisions
class eny_div():
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.Rect = pygame.Rect(self.x,self.y,self.w,self.h)

def main():
    pass



if __name__ == "__main__":
    main()