import os
import sys
import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((480,640))

FPS = 30
clock = pg.time.Clock()

asteroidtimer = 100
appletimer = 200
asteroids = [[20,0,0]]
apples = [[50,0]]
score = 0
credit = 3

try : 
    spaceshipimage = pg.image.load("./img/spaceship.png")
    asteroid1 = pg.image.load("./img/asteroid00.png")
    asteroid2 = pg.image.load("./img/asteroid01.png")
    asteroid3 = pg.image.load("./img/asteroid02.png")
    appleimage = pg.image.load("./img/apple.jpg")
    asteroidimage = [asteroid1,asteroid2, asteroid3]   
    gameover = pg.image.load("./img/gameover.jpg")

    #효과음 삽입
    takeoffsound = pg.mixer.Sound("./audio/takeoff.wav")
    landingsound = pg.mixer.Sound("./audio/landing.wav")
    #takeoffsound.play()

except Exception as arr :
    print("error open image")
    pg.quit()
    exit(0)

running = True
BACKGROUND_COLOR = (255,255,255)


def text(arg,x,y) :
    font = pg.font.Font(None, 24)
    text = font.render("score :" + str(arg).zfill(6), True, (0,0,0))
    textRect = text.get_rect()
    textRect.centerx = x
    textRect.centery = y
    screen.blit(text,textRect)

while running :
    screen.fill(BACKGROUND_COLOR)

    for event in pg.event.get() :
        keys = pg.key.get_pressed()
        if event.type == pg.QUIT or keys[pg.K_ESCAPE] :
            pg.quit()
            exit(0)
    text(score, 400,10)

    score +=  1
    if score % 100  == 0 :
        FPS += 1

    #spaceship 위치/그리기 
    position = pg.mouse.get_pos()
    if position[0] <= 480 :
        spaceshippos = (position[0],600)
        screen.blit(spaceshipimage , spaceshippos)

    #landingsound.play()

    #spaceship 사각형
    spaceshiprect = pg.Rect(spaceshipimage.get_rect())    
    spaceshiprect.left = spaceshippos[0]
    spaceshiprect.top = spaceshippos[1]

    asteroidtimer -= 10    
    appletimer -= 10

    if asteroidtimer <= 0 :
        asteroids.append([random.randint(5,475), 0, random.randint(0,2)])
        asteroidtimer = random.randint(50,200)        

    if appletimer <= 0 :
        apples.append([random.randint(5,475), 0])
        appletimer = random.randint(100,200)

    index = 0
    for stone in asteroids :
        stone[1] += 10
        if stone[1] > 640 :            
            asteroids.pop(index)

        stonerect = pg.Rect(asteroidimage[stone[2]].get_rect())
        stonerect.left = stone[0]
        stonerect.top = stone[1]

        if stonerect.colliderect(spaceshiprect) :
            asteroids.pop(index)
            print("colliderect")
            credit -= 1
            if credit == 0 : 
                running = False
        screen.blit(asteroidimage[stone[2]], (stone[0],stone[1]))
        index += 1
       
    appleindex = 0        
    for apple in apples :        
        apple[1] += 10        

        applerect = pg.Rect(appleimage.get_rect())
        applerect.left = apple[0]
        applerect.top = apple[1]

        if applerect.colliderect(spaceshiprect) :            
            score += 100
            apples.pop(appleindex)
          
        screen.blit(appleimage, (apple[0],apple[1]))        
        appleindex += 1

    clock.tick(FPS)
    pg.display.flip()

while 1 :
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            pg.quit()
            exit(0)

    pg.display.flip()