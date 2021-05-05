import pygame
import sys
import time
from pygame import mixer
pygame.init()
mixer.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption('amar')
font = pygame.font.SysFont(None, 40)
#sounds 
mixer.music.load("sounds/Ping_Pong_Ball_Hit.mp3")
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    win.blit(screen_text, [x,y])

 

def my_game():
    run=True
    clock=pygame.time.Clock()
    score=0
    score1=0
    
    gameover=False
    # rec
    rec3=200
    rec4=465
    #velocities of 2nd
    vel_y1=0
    vel_y2=0
    black=[0,0,0]
    red=[0,0,255]
    fps=30
    #ball
    ball_x=100
    ball_y=200
    ball_velx=9

    ball_vely=9

  
    while run:
        if gameover:
        
            win.fill(black)
            text_screen("game over!PRESS enter",[255,0,255],100,230)
            for event in pygame.event.get():
                
                if event.type==pygame.QUIT:
                    run=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        my_game()
        else:
            
        
            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    run=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        run=False
                    
                    if event.key==pygame.K_LEFT:
                        vel_y1=-6
                    if event.key==pygame.K_RIGHT:
                        vel_y1=6
        
        
            rec3+=vel_y1
            ball_x+=ball_velx
            ball_y+=ball_vely

            if ball_x>500 or ball_x<0:
                mixer.music.play()

                ball_velx*=-1
                
            
                
            
                
                
                
            if ball_y<0:
                mixer.music.play()



                ball_vely*=-1
            if  (ball_y+15)>=500:

                
                gameover = True
                
        
            

            
        
                
            if rec3>400:
                rec3=400
            if rec3<0:
                rec3=0
        
            




            
            
            win.fill(black)
            text_screen("SCORE: " + str(score),red, 195, 20)
            
            

            p2=pygame.draw.rect(win,[0,255,255],[rec3,rec4,80,20])
            b=pygame.draw.rect(win,[255,0,0],[ball_x,ball_y,15,15])  
        
            if  b.colliderect(p2) or (ball_x == rec3 and ball_y+15 ==rec4) or (ball_x ==rec3+80 and ball_y ==rec4):
                
                mixer.music.play()

                ball_vely*=-1
                score+=1
                
                print(score)
               
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

my_game()

