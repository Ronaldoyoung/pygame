import pygame as pg
from pygame import Rect

pg.init
screen = pg.display.set_mode((600,400))

def main() :
    done = False
    while not done :    
        screen.fill((255,255,255))
        for event in pg.event.get() :
            if event.type == pg.QUIT :
                done = True
        """ 1. """
        pg.draw.rect(screen, (0,0,0) , (50,50,10,100))

        """ 2. """
        r = Rect(100,100,10,100)        
        screen.fill((0,255,0) , r)

        """ 3 """
        image = pg.Surface([10,100]).convert_alpha()
        image.fill((0,0,255))
        rect = image.get_rect(center = (150,150))
        screen.blit(image,rect)

        pg.display.flip()


    print("done ", done)
    print("here")


if __name__ == '__main__' :
    main()


            