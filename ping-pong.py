from pygame import *
from random import randint
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self,imagep,x,y,size_x,size_y,speed):
        super().__init__()
        self.image=transform.scale(image.load(imagep),(size_x,size_y))
        self.speed=speed
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keyp=key.get_pressed()
        if keyp[K_w] and self.rect.y<win_h-80:
            self.rect.y+=self.speed
        if keyp[K_s] and self.rect.y>5:
            self.rect.y-=self.speed
    def update_r(self):
        keyp=key.get_pressed()
        if keyp[K_UP] and self.rect.y<win_h-80:
            self.rect.y+=self.speed
        if keyp[K_DOWN] and self.rect.y>5:
            self.rect.y-=self.speed
game_over=True
finish=False
win_w=1280
win_h=720
speed_y=3
speed_x=3
background = transform.scale(image.load("pole_dla ping ponga.jpg"), (win_w, win_h))
win=display.set_mode((win_w,win_h))
clock=time.Clock()
player1=Player('left.png',30,200,30,130,150)
player2=Player('right.png',1220,200,30,130,150)
katon_koboku_no_jutsu=GameSprite('ball.png',615,330,50,50,50)

while game_over:
    for e in event.get():
        if e.type==QUIT:
            game_over=False
    if finish==False: 
        win.blit(background,(0,0))
        player1.update_l()
        player2.update_r()
        player1.reset()
        player2.reset()
        katon_koboku_no_jutsu.reset()
    display.update()
    clock.tick(60)
