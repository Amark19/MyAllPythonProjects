import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.press(key)
    return

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(459, 476):
        for j in range(150, 193):
            if data[i, j] >100:
                hit("down")
                return
    

    for i in range(467, 485):
        for j in range(189, 223):
            if data[i, j] > 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(3)
    hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
            
        # print(asarray(image))
        
        # Draw the rectangle for cactus
        # for i in range(465, 483):
        #     for j in range(195, 222):
        #         data[i, j] = 0
        
        # # Draw the rectangle for birds
        # for i in range(459, 476):
        #     for j in range(150, 195):
        #         data[i, j] = 171

        # image.show()
        # break
      

