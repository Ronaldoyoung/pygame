import os
import sys
import pygame as pg
import random

BACKGROUD_COLOR = (50,50,60)
CAPTION = "snake Game"
SCREEN_SIZE = (500,500)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

pg.init()
pg.display.set_caption(CAPTION)
screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()
ftp = 120.0
game_speed = 30
done = False
matrix = []
rows = 12
cols = 12
cell_size = 40
cell_margin = 1
snake_coor = []
apple = []
dir_r,dir_c = 1,0
direction = ""
credit = 3
score = 0

try : 
    apple_image = pg.image.load("./img/apple.jpg")
    gameover = pg.image.load("./img/gameover.jpg")

except Exception as arr :
    print("그림 삽입이 잘못 되었습니다.")
    pg.quit()   

def forward() :
    global score, game_speed
    check_collision()
    r,c = snake_coor[0]
    r += dir_r
    c += dir_c
    snake_coor.insert(0, (r,c))
    snake_coor.pop(-1)       
    if snake_coor[0] == apple[0] : 
        snake_eat_apple()
        score += 100
        if score == 500 : game_speed = 15


def check_collision() :
    global credit
    r,c = snake_coor[0]
    if matrix[r][c] == 9 or len(snake_coor) > 2 and snake_coor[0] in snake_coor[1:] :
       credit -= 1
       snake_coor.clear()
       game_init_data()       


def getRndApple():
    global apple
    r = random.randint(1,10)
    c = random.randint(1,10)
    apple = [(r,c)]
    if apple[0] in snake_coor :        
        getRndApple()    


def game_init_data() :
    global dir_r, dir_c, direction
    snake_coor.append((1,1))
    dir_r,dir_c = 1,0
    direction = "RIGHT"
    board_init()    
    

def board_init() :
    onerow = []
    for i in range(rows) :
        for j in range(cols) :
            onerow.append(9) if j == 0 or j == (cols - 1) or i == 0 or i == (rows -1 ) else onerow.append(0)
        matrix.append(onerow)
        onerow = []


def object_draw_board() :
    for r in range(rows) :
        for c in range(cols) :
            color = BLACK if matrix[r][c] == 9 else BLUE
            pg.draw.rect(screen, color, (c *(cell_size + cell_margin), r * (cell_size + cell_margin), cell_size, cell_size))


def object_draw_snake() : 
    for idx, pos in enumerate(snake_coor) :
        color = RED if idx == 0 else GREEN
        c = pos[0]; r = pos[1]
        pg.draw.rect(screen, color , (c * (cell_size + cell_margin), r * (cell_size + cell_margin) , cell_size, cell_size ))


def snake_eat_apple() :
    global snake_coor    
    a = snake_coor[-1][:]
    snake_coor.append(a)    


def object_draw_apple() :    
    if snake_coor[0] == apple[0] :
        getRndApple();        
    rect = apple_image.get_rect()
    r = apple[0][0] ; c = apple[0][1]
    rect.centerx = 60 + (40 * (r-1) + r)  
    rect.centery = 60 + (40 * (c-1) + c)  
    screen.blit(apple_image, rect)


def object_draw_status(x,y) :
    global done
    if credit == 0 :
        done = True
    font = pg.font.SysFont("comicsansms",24)
    scoreSurf = font.render("score:" + str(score).zfill(6) + "  credit:" + str(credit), True, (0,255,0))
    surfRect = scoreSurf.get_rect()
    screen.blit(scoreSurf,surfRect) 
    

def set_Dir(r,c) :
    global dir_r, dir_c
    dir_r = r
    dir_c = c


def process_key(key) :
    global direction
    if key == pg.K_UP and not direction == "DOWN":
        set_Dir(0,-1)
        direction = "UP"
    elif key == pg.K_DOWN and not direction == "UP":
        set_Dir(0,1)
        direction = "DOWN"
    elif key == pg.K_LEFT and not direction == "RIGHT":
        set_Dir(-1,0)
        direction = "LEFT"
    elif key == pg.K_RIGHT and not direction == "LEFT":
        set_Dir(1,0)
        direction = "RIGHT"
    else :
        pass


def event_loop() :
    global done
    for event in pg.event.get():
        keys = pg.key.get_pressed()
        if event.type == pg.QUIT or keys[pg.K_ESCAPE] :                        
            done = True            
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1 :
            pass
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:    
            print("Mouse clik")
        elif event.type == pg.KEYDOWN :            
            process_key(event.key)


def main_loop ():
    global done ,apple
    count = 0
    getRndApple()
    while not done :
        event_loop()       
        if count % game_speed == 0 :
            forward()
            count = 0
        screen.fill(BACKGROUD_COLOR)
        object_draw_board()
        object_draw_status(400,30)        
        object_draw_snake()
        object_draw_apple()        
        pg.display.update()
        count += 1
        clock.tick(ftp)


def image_draw_gameover() :
    gameoverRect = gameover.get_rect()
    print("gameoverRect: " , gameoverRect)
    screen.blit(gameover, gameoverRect)
    pg.display.update()


def main() :
    print("Game Start")   
    game_init_data()
    main_loop()
    image_draw_gameover()
    input('아무키나 누르세요')
    

if __name__ == "__main__" : 
    main()


