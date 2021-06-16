import pygame
import random
from random import randint
pygame.init()

Width, Height = 600, 500
win = pygame.display.set_mode((Width, Height))

pygame.display.set_caption("Space invaders")


class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y 
        self.w = w 
        self.h = h
        self.Rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.img = pygame.image.load(r"C:\Users\siaaa013\Documents\Programering\python\Games\Spaceinvaders\bullet.png")
    def move(self):
        self.y -= 5

    def draw(self,win):
        win.blit(self.img, (self.x, self.y))
        
class Player():
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hit = False
        self.Rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.img = pygame.image.load(r"C:\Users\siaaa013\Documents\Programering\python\Games\Spaceinvaders\player.png")
    def draw(self,win):
        if self.hit == False:
            win.blit(self.img,(self.x, self.y))
    def collide(self):
        self.hit = True
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.x = x 
        self.y = y 
        self.w = w 
        self.h = h 
        self.hit = False
        self.Rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.img = pygame.image.load(r"C:\Users\siaaa013\Documents\Programering\python\Games\Spaceinvaders\enemy.png")
    def gotorandom(self):
        self.x = randint(Width)
        self.Rect.move_ip(self.x, self.y)
    def draw(self, win):
        if self.hit == False:
            win.blit(self.img, (self.x, self.y))
    def collide(self):
        self.hit = True
    def move(self):
        self.y += 0.0
        self.Rect.move_ip(self.x, self.y)

def redraw(sprites):
    for i in sprites:
        i.draw(win)
    pygame.display.update()


def main():
    bg = pygame.image.load(r"C:\Users\siaaa013\Documents\Programering\python\Games\Spaceinvaders\bg.png")
    sprites = []
    bullets = []
    enemys = []
    #create lots of bullets clones
    all_bullets = pygame.sprite.Group()
    
    all_enemys = pygame.sprite.Group()

    player = Player(400,470,25,25)
    sprites.append(player)
    FPS = 60
    clock = pygame.time.Clock()
    run = True 
    bullettimer = 0
    #main loop
    for i in range(5):
        x,y,w,h = randint(1, Width),20, 25, 25
        new_enemy = Enemy(x,y,w,h)
        all_enemys.add(new_enemy)
        sprites.append(new_enemy)
        enemys.append(new_enemy)
        
    #main loop 
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("the program got closed")
                run = False
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            player.x -= 4
            player.Rect.move_ip(player.x, player.y)
        if keys[pygame.K_d]:
            player.x += 4
            player.Rect.move_ip(player.x, player.y)        
        if keys[pygame.K_SPACE]:
            if bullettimer > 30:
                x,y = player.x + player.w/2, player.y
                w,h = 8,10
                new_bullet = Bullet(x,y,w,h)
                all_bullets.add(new_bullet)
                sprites.append(new_bullet)
                bullets.append(new_bullet)
    
                bullettimer = 0
                
        for i in enemys:
            for j in bullets:
                if i.Rect.colliderect(j.Rect):
                    i.hit = True
                    print("hit")
                    
        for i in enemys:
            i.move()
            
        for i in bullets:
            i.Rect = i.x, i.y, i.w, i.h
            if i.y <= -5:
                i.kill()
                bullets.remove(i)
                sprites.remove(i)
                print("just killed a spirte")
            i.move()
            
            
        win.blit(bg,(0,0))

        redraw(sprites)

        bullettimer += 1
    pygame.quit()

if __name__ == "__main__":
    main()
        
