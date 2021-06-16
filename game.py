# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 14:16:40 2021

@author: siaaa013
"""
#TODO get it to work

import pygame

import math





division_img = pygame.image.load("DIVISION.png")
division_img_sel = pygame.image.load("DIVISION_SELECTED.png")
pointer_img = pygame.image.load("POINTER.png")
pointer_img_atk = pygame.image.load("POINTER_ATTACK.png")
        
    

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

class Pointer(object):
    def __init__(self, x, y, height, width, img, attack_img, number):
        self.x = x
        self.y = y
        self.h = height
        self.w = width
        self.img = img
        self.attack_img = attack_img
        self.number = number
        self.attack = False
        
    def goto_mouse(self,):
        self.x, self.y = pygame.mouse.get_pos()

        
    def draw(self, win):
        if self.attack == False:
            win.blit(self.img, (self.x, self.y))
        else:
            win.blit(self.sel_img, (self.x, self.y))
        
        
        

class Division(object):
    def __init__(self, x,y,height,width,image, sel_image, number):
        self.x = x
        self.y = y
        self.h = height
        self.w = width
        self.selected = False
        self.img = image
        self.sel_img = sel_image
        self.cw_img = image
        self.cw_sel_img = sel_image
        self.hitbox = x, width, y, height
        self.number = number
        self.angle = 0
        self.vel = 0.5
        self.goto = False
        self.point_x = False
        self.point_y = False
    def in_hitbox(self, x, y):
        #cheks if cord is in hitbox to sprite
        if x >= self.x and x <= self.x + self.w:
            if y >= self.y and y <= self.y + self.h:
                return True 
            
            
    def selecting(self):
        #tests if a division is being seleccted
        x,y = pygame.mouse.get_pos()
        if pygame.MOUSEBUTTONUP:
            if self.in_hitbox(x, y) and self.selected == False:
                self.selected = True
                self.goto = False

            
            elif self.selected == True and self.in_hitbox(x,y):
                self.selected = False
            else:
                if self.selected == True and not self.in_hitbox(x,y):
                    return True

    def de_selecting(self):
        self.selected = False

    def turn_division(self, x, y) :
        angle = turn(x, y, self.x, self.y, self.angle)

        
        angle = self.angle - angle
        self.cw_img, self.cw_sel_img, rect = rot_center(self.img,self.sel_img, angle, self.x, self.y)
        
    def goto_point(self):
        if self.goto == True:
            if self.point_x > self.x:
                self.x += self.vel
            if self.point_x < self.x:
                self.x -= self.vel
            
            if self.point_y > self.y:
                self.y += self.vel
            if self.point_y < self.y:
                self.y -= self.vel 
            
            if self.point_x == self.x and self.point_y == self.y:
                self.goto = False
        
        
          
    def draw(self, win):
        if not self.selected == True:
            win.blit(self.cw_img, (self.x, self.y))
        else:
            win.blit(self.cw_sel_img, (self.x, self.y))

def make_div(x, y,current_num):

    height = 25
    width = 25
    div = Division(x,y,height,width,division_img, division_img_sel, current_num)
    return div

def make_pointer(x, y, current_num):
    height = 15
    width = 15
    pointer = Pointer(x,y,height, width, pointer_img, pointer_img_atk, current_num)
    return pointer
        
   



    
    

