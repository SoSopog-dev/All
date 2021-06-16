# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 09:25:26 2021

@author: siaaa013
"""
import pygame
import math

def turn(touch_x, touch_y, centre_x, centre_y, angle):
   
    delta_x = touch_x - centre_x
    delta_y = touch_y - centre_y
    angle = math.atan2(delta_y, delta_x) * 180/math.pi

   
    return angle

def rot_center(image, sel_image, angle, x, y):
   
    rotated_sel_image = pygame.transform.rotate(sel_image, angle)
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, rotated_sel_image,  new_rect

class div(object):
    def __init__(self, x,y,width,height):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.sel = False
        
        self.hitbox = pygame.Rect(self.x,self.y,self.w,self.h)
        
        self.img = "img"
        self.sel_img = "sel_img"
        self.ci = self.img
        self.csi = self.sel_img
    
    def select(self):
        x,y = pygame.mouse.get_pos()
        
    def turn_division(self, x, y) :
        angle = turn(x, y, self.x, self.y, self.angle)
        angle = self.angle - angle
        self.cw_img, self.cw_sel_img, self.hitbox = rot_center(self.img,self.sel_img, angle, self.x, self.y)
        
    def draw(self, win):
        if self.sel == True:
            win.blit(self.csi, (self.x, self.y))
        else:
            win.blit(self.si, (self.x, self.y))
        
        