import pygame
import sys
import time
from pygame import mixer
pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption('DIDI')
run=True
white=[255,255,255]
red=[255,0,0]
O=pygame.image.load(r'C:\Users\HP\Downloads\my pyhton projects\o.jpg').convert()
x=pygame.image.load(r'C:\Users\HP\Downloads\my pyhton projects\x.jpg').convert()
font = pygame.font.SysFont(None, 60)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    win.blit(screen_text, [x,y])


win.fill(white)

x1,y1=80,120
x2,y2=190,220
x3,y3=310,320
x4,y4=82,118
x5,y5=192,218
x6,y6=312,318
while run:
    for event in pygame.event.get():

        if event.type==pygame.QUIT:

        
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                run=False
            ###for o#3
            if event.key==pygame.K_1:
                y1=120
                win.blit(O,(x1,y1))
                x1+=1
                y1+=1
            if event.key==pygame.K_2:
                y1=120
                win.blit(O,(x2,y1))
                x2+=1
                y1+=1
            if event.key==pygame.K_3:
                y1=120
                win.blit(O,(x3,y1))
                x3+=1
                y1+=1
            if event.key==pygame.K_4:
                y2=220
                win.blit(O,(x1,y2))
                x1+=1
                y2+=1
            if event.key==pygame.K_5:
                y2=220
                win.blit(O,(x2,y2))
                x2+=1
                y2+=1
            if event.key==pygame.K_6:
                y2=220
                win.blit(O,(x3,y2))
                x3+=1
                y2+=1
            if event.key==pygame.K_7:
                y3=320
                win.blit(O,(x1,y3))
                x1+=1
                y3+=1
            if event.key==pygame.K_8:
                y3=320
                win.blit(O,(x2,y3))
                x2+=1
                y3+=1
            if event.key==pygame.K_9:
                y3=320
                win.blit(O,(x3,y3))
                x3+=1
                y3+=1            

             #####for x###   
            if event.key==pygame.K_KP1:
                y4=118
                win.blit(x,(x4,y4))
                x4+=1
                y4+=1
            if event.key==pygame.K_KP2:
                y4=118
                win.blit(x,(x5,y4))
                x5+=1
                y4+=1
            if event.key==pygame.K_KP3:
                y4=118
                win.blit(x,(x6,y4))
                x6+=1
                y4+=1 
            if event.key==pygame.K_KP4:
                y5=218
                win.blit(x,(x4,y5))
                x4+=1
                y5+=1
            if event.key==pygame.K_KP5:
                y5=218
                win.blit(x,(x5,y5))
                x5+=1
                y5+=1
            if event.key==pygame.K_KP6:
                y5=218
                win.blit(x,(x6,y5))
                x6+=1
                y5+=1 
            if event.key==pygame.K_KP7:
                y6=318
                win.blit(x,(x4,y6))
                x4+=1
                y6+=1
            if event.key==pygame.K_KP8:
                y6=318
                win.blit(x,(x5,y6))
                x5+=1
                y6+=1
            if event.key==pygame.K_KP9:
                y6=318
                win.blit(x,(x6,y6))
                x6+=1 
                y6+=1
        
    if ((x1==81 and y1==121) and ( x2==191 and y1==121 ) and (x3==311 and  y1==121)):
        # print("win")
        text_screen("O WINS",red, 180, 20)
    if (x4==83 and x5==193 and x6==313) or (y4==119 and y5==219 and y6==319):
        # print("win")
        text_screen("X WINS",red, 180, 20)
       
    pygame.draw.line(win,[255,0,0],(170,100),(170,400))
    pygame.draw.line(win,[255,0,0],(310,100),(310,400))
    pygame.draw.line(win,[255,0,0],(80,190),(400,190))
    pygame.draw.line(win,[255,0,0],(80,300),(400,300))
    # print(x1)
    pygame.display.update()
    #clock.tick(fps)

pygame.quit()
quit()