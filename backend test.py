import pyautogui
import keyboard as key
from PIL import ImageGrab
from PIL import Image
import pygame

pygame.init()

swidth, sheigth = pyautogui.size()

win = pygame.display.set_mode((swidth,sheigth))

pygame.display.set_caption("RAT")




def PrtScn():
    width, heigth = pyautogui.size()
    run = True
    while run:
        if key.is_pressed("p"):
            bbox = 0, 0, width, heigth
            screenshot = ImageGrab.grab(bbox)
            screenshot.save(r"C:\Users\siaaa013\Documents\Programering\python\backdoor\image.png")


sc = pygame.image.load(r"C:\Users\siaaa013\Documents\Programering\python\backdoor\image.png")




def redraw(win):
    win.blit(sc,(0,0))
    pygame.display.update()



#main loop

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()

    sc = pygame.image.load(r"C:\Users\sigur\OneDrive\Bilder\Kamerabilder\image.png")



    redraw(win)
        




    
pygame.quit()
