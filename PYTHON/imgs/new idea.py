import pygame
import sys
from pygame import mixer
import time
import datetime
import sys

pygame.init()
mixer.init()
win=pygame.display.set_mode((338,500))
pygame.display.set_caption('amar')
#img
bse=pygame.image.load('gallery/flappy/base.png').convert()
bckgnd=pygame.image.load('gallery/flappy/bg.png').convert()
pipes=pygame.image.load('gallery/flappy/pipe.png').convert()
player=pygame.image.load('gallery/flappy/bird2.png').convert()
player1=pygame.image.load('gallery/flappy/bird3.png').convert()
go=pygame.image.load('gallery/flappy/gameover.png').convert()
ntr=pygame.image.load('gallery/flappy/enter.png').convert()
##sound effect
# a=pygame.mixer.Sound("sounds/die.mp3")
# b=mixer.music.load("sounds/point.mp3")
# c=mixer.music.load("sounds/swoosh(1).mp3")
# d=mixer.music.load("sounds/wing.mp3")
font = pygame.font.SysFont(None, 30)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    win.blit(screen_text, [x,y])

def my_gme():
    run=True
    clock=pygame.time.Clock()
    init=time.time()
    #positons
    pos_x=20
    pos_y=380

    vel_x=0
    vel_y=0
    black=[0,0,0]
    red=[235,0,0]
    #background pos
    x1=1
    x3=336
    #base pos
    x2=1
    x4=336
    #obstacle pos
    x5=180
    x6=507
    y5=340
    score=0
    z=0
    gamespeed = True
    gameover=False
    fps=200


    
    while run:
        if gameover:
            
            
            
            
            
            for event in pygame.event.get():
                
                if event.type==pygame.QUIT:
                    run=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        run = False
                    if event.key==pygame.K_RETURN:
                        my_gme()
        else:
            for event in pygame.event.get():

                if event.type==pygame.QUIT:

                
                    run=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        run = False
                    if event.key==pygame.K_UP or event.key==pygame.K_SPACE :
                        vel_y=-2
                        vel_x=0
                        walk=True
            pos_y+=vel_y
            pos_x+=vel_x
            if pos_y<240 and pos_x==169:
                pos_y=240
                
            if pos_y<365:
                walk=False
            if pos_y==240:
                vel_y=2
                
            if pos_y>370:
                pos_y=370

         
            win.blit(bckgnd,(x1,0))
            x1-=1
            if x1==-334:
                x1=336
            win.blit(bckgnd,(x3,0))
            x3-=1
            if x3==-334:
                x3=336
            x=pygame.draw.rect(win,[0,255,0],[x5,y5,24,320])
            win.blit(pipes,(x5,y5))
            
            x5-=1
            if x5==-169:
                x5=507
            y=pygame.draw.rect(win,[0,255,0],[x6,y5,24,320])
            win.blit(pipes,(x6,y5))
            
            x6-=1
            if x6==-169:
                x6=507

            win.blit(bse,(x2,390))
            x2-=1
            if x2==-334:
                x2=336
            win.blit(bse,(x4,390))
            x4-=1
            if x4==-334:
                x4=336
            
            

            
            
            p=pygame.draw.rect(win,[128,128,0],[pos_x+5,pos_y+1,24,22])
            if p.colliderect(x) or p.colliderect(y):
                win.blit(go,(100,50))
                win.blit(ntr,(50,170))
                # pygame.mixer.Channel(0).play(pygame.mixer.Sound('die.mp3'))
                gameover = True
                
                
            win.blit(player,(pos_x,pos_y))
            text_screen("SCORE:"+str(score),red, 225, 50)
        
            if time.time() - init>10:
                
                fps=250
            if time.time() - init>10:
                
                fps=300
            
            if abs(y5 - pos_y)>95:
                score+=1
          
                
                
            pygame.display.update()
            clock.tick(fps)
    

        
        
    pygame.quit()
    quit
if __name__ == "__main__":
    
    my_gme()