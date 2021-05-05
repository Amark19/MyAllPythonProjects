import pygame
import sys
from pygame import mixer
pygame.init()
mixer.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption('amar')
run=True
clock=pygame.time.Clock()
score=0
score1=0
font = pygame.font.SysFont(None, 30)
#sounds 
mixer.music.load("sounds/Ping_Pong_Ball_Hit.mp3")
#2nd rec
rec1=475
rec2=200
x1=20
y1=80
#1st rec
rec3=5
rec4=200
#velocities of 2nd
vel_y1=0
vel_y2=0
black=[0,0,0]
red=[0,0,255]
fps=25
#ball
ball_x=100
ball_y=200
ball_velx=9

ball_vely=9

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    win.blit(screen_text, [x,y])   
while run:
    for event in pygame.event.get():

        if event.type==pygame.QUIT:

        
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                run=False
            
            if event.key==pygame.K_UP:
               vel_y1=-4
            if event.key==pygame.K_DOWN:
                vel_y1=4
            if event.key==pygame.K_1:
                vel_y2=-4
            if event.key==pygame.K_2:
                vel_y2=4
    rec2+=vel_y1
    rec4+=vel_y2
    ball_x+=ball_velx
    ball_y+=ball_vely
    if ball_x>500:
        ball_velx*=-1
        mixer.music.play()
        score+=1
    
        
    if ball_x<0:
        ball_velx*=-1
        mixer.music.play()
        score1+=1
      
        

        
        
    if ball_y<0  or ball_y>500:
        mixer.music.play()


        ball_vely*=-1
    rec2+=vel_y1
    rec4+=vel_y2

       
    if rec2<0:
        rec2=0
    if rec4>420:
        rec4=420
    if rec4<0:
        rec4=0
    if rec2>421:
        rec2=420
    




    
    
    win.fill(black)
    text_screen( str(score1),red, 260, 5)
    text_screen( str(score),red, 190, 5)
    p1=pygame.draw.rect(win,[255,0,255],[rec1,rec2,x1,y1])    
    p2=pygame.draw.rect(win,[0,255,255],[rec3,rec4,20,80])
    b=pygame.draw.rect(win,[255,0,0],[ball_x,ball_y,15,15])  
    pygame.draw.line(win,[255,255,0],(250,0),(250,500))
    if b.colliderect(p1) or b.colliderect(p2):
        mixer.music.play()
        ball_velx*=-1
        
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
