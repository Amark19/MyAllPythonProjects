import random
import sys
import pygame
from  pygame.locals import *
#global variables
run=True
basex=0
fps=32
scr_wid=288
scr_ht=512
win=pygame.display.set_mode((scr_wid,scr_ht))
GNDY=scr_ht*0.8
GAME_flappy={}
PLAYER='gallery/flappy/bird1.png'
BACKGROUND='gallery/flappy/bg.png'
PIPE='gallery/flappy/pipe.png'
def welcomescr():
    playerx=int(scr_wid/5)
    playery=int((scr_ht - GAME_flappy['player'].get_height())/2)
       
    basex=0
    while run:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                return
            else:
                win.blit(GAME_flappy['background'],(0,0))
                
                win.blit(GAME_flappy['player'],(playerx,playery))
                
                win.blit(GAME_flappy['base'],(int(basex),int(GNDY)))
                
                pygame.display.update()
                fpsclock.tick(fps)
def maingame():
    score=0
    playerx=int(scr_ht/5)
    playery=int(scr_ht/2)
    basex=0
    #create two pipes
    Pipe1=getRandompipe()
    Pipe2=getRandompipe()
    #list of upper pipes
    upperpipes=[
        {'x':scr_wid+200,'y':Pipe1[0]['y']},
        {'x':scr_wid+200+(scr_wid/2),'y':Pipe1[0]['y']},
    ]
    #list of lower pipes
    lowerpipes=[
        {'x':scr_wid+200,'y':Pipe2[1]['y']},
        {'x':scr_wid+200+(scr_wid/2),'y':Pipe2[1]['y']},
    ]
    pipeVelx=-4
    playerVelY=-9
    playerMaxVelY=10
    playerMinVelY=-8
    playerAccY=1
    playerFlapAccv=-8
    playerflapped=False
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                if playery>0:
                    playerVelY=playerFlapAccv
                    playerflapped=True
        crashtest=iscollide(playerx,playery,upperpipes,lowerpipes) 
        if crashtest:
            return
        if playerVelY<playerMaxVelY and not playerflapped:
            playerVelY+=playerAccY
        if playerflapped:
            playerflapped=False
        playerHeight=GAME_flappy['player'].get_height()
        playery+=min(playerVelY,GNDY-playery-playerHeight)
        #move pipes to left
        for upperpipe,lowerpipe in zip(upperpipes,lowerpipes):
            upperpipe['x']+=pipeVelx
            lowerpipe['x']+=pipeVelx


        if 0<upperpipes[0]['x']<5:
            newpipe=getRandompipe()
            upperpipes.append(newpipe[0])
            lowerpipes.append(newpipe[1])

        if upperpipes[0]['x']<-GAME_flappy['pipe'][0].get_width():
            upperpipes.pop(0)
            lowerpipes.pop(0)
        win.blit(GAME_flappy['background'],(0,0))
        for upperpipe,lowerpipe in zip(upperpipes,lowerpipes):
            win.blit(GAME_flappy['pipe'][0],(int(upperpipe['x']),int(upperpipe['y'])))
            win.blit(GAME_flappy['pipe'][1],(int(lowerpipe['x']),int(lowerpipe['y'])))
           
          

        win.blit(GAME_flappy['base'],(basex,GNDY))
        win.blit(GAME_flappy['player'],(playerx,playery))
        pygame.display.update()
        fpsclock.tick(fps)


def iscollide(playerx,playery,upperpipes,lowerpipes):
    if playery>GNDY-25 or playery<0:
        return True
    for pipe in upperpipes:
        pipeheight=GAME_flappy['pipe'][0].get_height()
        if(playery<pipeheight+pipe['y']and abs(playerx  - pipe['x'])<GAME_flappy['pipe'][0].getwidth()):
            return True
    return False
def getRandompipe():
    pipeheight=GAME_flappy['pipe'][0].get_height()
    offset=scr_ht/3
    y2=offset+random.randrange(0,int(scr_ht-GAME_flappy['base'].get_height()-1.2*offset))
    pipex=scr_wid+10
    y1=pipeheight-y2+offset
    pipe=[
    
        {'x':pipex,'y':-y1},#upper pipe
        {'x':pipex,'y':y2}#lower pipe
    ]
    return pipe
if __name__ == "__main__":
    pygame.init()
    fpsclock=pygame.time.Clock()
    pygame.display.set_caption('flappy bird by amar')
        
    GAME_flappy['base']=pygame.image.load('gallery/flappy/base.png').convert_alpha()
    GAME_flappy['pipe']=(pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),      
    pygame.image.load(PIPE).convert_alpha() 
    )
    GAME_flappy['background']=pygame.image.load(BACKGROUND).convert_alpha()
    GAME_flappy['player']=pygame.image.load(PLAYER).convert_alpha()
    
    while run:
        welcomescr()
        maingame()
        getRandompipe()