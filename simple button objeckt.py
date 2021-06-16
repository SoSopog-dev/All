#chess game
import pygame



class button(object):
    def __init__(self, x, y, w, h, type, picture):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.type = type
        self.picture = picture
        self.Rect = pygame.Rect(x,y,w,h)
    def select():
        x,y = pygame.get_pos()
        if self.Rect.collidepoint(x,y):
            #do the thing the button should do
        else:
            pass
    def draw(self,win):
        win.blit(self.picture, (self.x,self.y))     
#main function      
def main():
    run = True 
    #main loop
    while run:
        pass
