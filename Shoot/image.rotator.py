import pygame as pg
import math

class Rotator:
    def __init__(self, screen_rect) :
        self.orig_image = pg.Surface([10,100]).convert_alpha()        
        self.image = self.orig_image
        self.image.fill((255,0,0)) 
        self.rect = self.image.get_rect(center=screen_rect.center)                
        self.angle = 0
        self.distance = 0
        self.angle_offset = 0
    

    def render(self, screen) :
        screen.blit(self.image, self.rect)


    def get_angle(self):
        mouse = pg.mouse.get_pos()
        offset = (self.rect.centerx-mouse[0],self.rect.centery-mouse[1])        
        self.angle = math.degrees(math.atan2(*offset)) - self.angle_offset        
        old_center = self.rect.center
        self.image = pg.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(center=old_center)
        self.distance = math.sqrt((offset[0] * offset[0]) + (offset[1] * offset[1]))
         
    def update(self):
        self.get_angle()
        self.display = 'angle:{:.2f} disatance:{:.2f}'.format(self.angle, self.distance)
        print("display " , self.display)


if __name__ == '__main__' :
    running = True
    pg.init()
    screen = pg.display.set_mode((600,400))
    screen_rect = screen.get_rect()    
    rotator = Rotator(screen_rect)
    clock = pg.time.Clock()

    while running:
        screen.fill((0,0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT :
                running = False
        rotator.update()
        rotator.render(screen)
        pg.display.update()
        clock.tick(60)