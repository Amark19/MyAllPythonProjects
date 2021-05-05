from pygame import mixer
import time
import datetime
mixer.init()


init=time.time()
waterdrink=10
eyetime=7
extime=9

run=True
while run:
    if (time.time() - init)>waterdrink:
        
        mixer.music.load("sounds/water.mp3")
        mixer.music.play()
        with open("water.py",'a') as f:
                f.write(f"u r  drinking time is={datetime.datetime.now()}\n")
               
        waterdrink+=10
    if (time.time() - init)>eyetime:

        mixer.music.load("sounds/eye.mp3")
        mixer.music.play()      
        with open("eye.py",'a') as f:
                f.write(f"u r  eye exercise time is={datetime.datetime.now()}\n")
        eyetime+=7
    if (time.time() - init)>extime:
        mixer.music.load("sounds/exer.mp3")
        mixer.music.play()
        with open("exercise.py",'a') as f:
                f.write(f"u r  physical exercise  time is={datetime.datetime.now()}\n")
        
        extime+=9
    if (time.time() - init)>60:
        run=False
    


       



