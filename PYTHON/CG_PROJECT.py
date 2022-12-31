import pygame
import time
import os
from pygame import mixer
pygame.init()
mixer.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('amar')
# vlues
# img
font = pygame.font.SysFont(None, 30)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    win.blit(screen_text, [x, y])


def gameloop():
    path = "A:\Projects\MyAllPythonProjects"
    player = pygame.image.load(f'{path}\PYTHON\imgs\gallery\player.png')
    bg = pygame.image.load(f'{path}\PYTHON\imgs\gallery\highway.png')
    bg1 = pygame.image.load(f'{path}\PYTHON\imgs\gallery\highway.png')
    e2 = pygame.image.load(f'{path}\PYTHON\imgs\gallery\enemy.png')
    e1 = pygame.image.load(f'{path}\PYTHON\imgs\gallery\enemy.png')
    e3 = pygame.image.load(f'{path}\PYTHON\imgs\gallery\enemy.png')
    gameover = False
    black = [0, 0, 0]
    run = True
    vel = 8
    # 1st obstacle
    x1 = 240
    y1 = -12
    # 2nd obstacle
    x2 = 350
    y2 = 12
    # 3rd obstacle
    x3 = 50
    y3 = 240
    # 4th nobsatcle
    x4 = 240
    y4 = -100
    # 5th nobsatcle
    x5 = 150
    y5 = 50
    # 6th nobsatcle
    x6 = 420
    y6 = 100
    # player
    r1 = 240
    r2 = 470
    vel_x1 = 0
    vel_y1 = 0
    vel_x2 = 0
    vel_y2 = 0
    # highway
    vel_highx = 0
    vel_highy = 0
    vel_highx1 = 0
    vel_highy1 = -500
    fps = 50
    clock = pygame.time.Clock()

    while run:
        if gameover:
            win.fill(black)
            text_screen("Game Over! Press Enter To Continue",
                        [255, 0, 0], 50, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                    elif event.key == pygame.K_RIGHT:
                        vel_y1 = 3
                        vel_x1 = 0
                    elif event.key == pygame.K_LEFT:
                        vel_y1 = -3
                        vel_x1 = 0
                    elif event.key == pygame.K_UP:
                        vel_x1 = -3
                        vel_y1 = 0
                    elif event.key == pygame.K_DOWN:
                        vel_x1 = 3
                        vel_y1 = 0
            r1 += vel_y1
            r2 += vel_x1

            y1 += vel
            y2 += vel
            y4 += vel
            y5 += vel

            if r1 <= 70:
                r1 = 70
            if r1 >= 400:
                r1 = 400
            if r2 <= 0:
                r2 = 0
            if r2 >= 440:
                r2 = 440
            if y1 >= 510:
                y1 = -12
            if y2 >= 510:
                y2 = -20
            if y4 >= 510:
                y4 = -100
            if y5 >= 510:
                y5 = -50
            if (y1-75 == y4):
                y1 = 80

            win.fill(black)

            if vel_highy == 500:
                vel_highy = -500
            if vel_highy1 == 500:
                vel_highy1 = -500

            win.blit(bg, (vel_highx, vel_highy))
            win.blit(bg1, (vel_highx1, vel_highy1))
            vel_highy += 2
            vel_highy1 += 2
            v1 = pygame.draw.rect(win, [255, 0, 0], [x1, y1, 33, 65])
            win.blit(e1, (x1, y1))
            v2 = pygame.draw.rect(win, [255, 0, 0], [x2, y2, 33, 65])
            win.blit(e3, (x2, y2))
            v4 = pygame.draw.rect(win, [255, 0, 0], [x4, y4, 33, 65])
            win.blit(e2, (x4, y4))
            v5 = pygame.draw.rect(win, [255, 0, 0], [x5, y5, 33, 65])
            win.blit(e2, (x5, y5))

            p1 = pygame.draw.rect(win, [128, 128, 0], [r1, r2, 30, 65])
            win.blit(player, (r1, r2))
            if p1.colliderect(v1) or p1.colliderect(v2) or p1.colliderect(v4) or p1.colliderect(v5):
                # text_screen("Game Over! Press Enter To Continue", [255,0,0], 100, 250)
                gameover = True

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


gameloop()
