import pygame as pg
from pygame.locals import *
import sys
import math
import numpy as np
import random

RED = (255,0,0)

class Gun :
    def __init__(self) :
        print("Gun create")
        self.orig_image = pg.Surface([15,300]).convert_alpha()
        self.image = self.orig_image
        self.image.fill(RED)
        self.rect = self.image.get_rect(center = (game.screen_rect.centerx,game.screen_rect.bottom))
        self.angle = 0


    def render(self):
        game.screen.blit(self.image, self.rect)


    def update(self) :
        mouse = pg.mouse.get_pos()
        offset = (self.rect.centerx - mouse[0], self.rect.bottom - mouse[1])
        self.angle = math.degrees(math.atan2(*offset))
        old_center = self.rect.center
        self.image = pg.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(center = old_center)



class GameMain :
    running = True
    bullet = []
    gmaeImage = []
    def __init__(self, width = 600, height = 500 , bgcolor = None):        
        pg.init()
        self.width,self.height = width , height
        self.screen = pg.display.set_mode((self.width,self.height))
        self.screen_rect = self.screen.get_rect()

        self.bgcolor = (50,50,50)

        self.clock = pg.time.Clock()
        self.limite_fps_max = 60
        self.game_init()        


    def game_init(self):
        self.gmaeImage = []


    def loop(self) :
        while self.running :
            self.handle_event()
            self.update()
            self.draw()


    def update(self):
        gun.update()


    def handle_event(self) :
        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:                                
                self.running = False
                sys.exit()
            elif event.type == KEYDOWN:
                if (event.key == K_ESCAPE):
                    self.running = False
            elif event.type == MOUSEBUTTONUP and event.button == 1 :
                pos = pg.mouse.get_pos()


    def draw(self) :
        self.screen.fill(self.bgcolor)
        pg.draw.circle(self.screen, RED, (self.screen_rect.centerx,self.screen_rect.bottom), 50)
        gun.render()
        pg.display.flip()



if __name__ == '__main__' :
    game = GameMain()
    gun = Gun()
    game.loop()

