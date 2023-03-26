import pygame as pg
import random

BLACK = [70] * 4
RED = [255] * 3
W, H = 500,500


pg.init()
win = pg.display.set_mode((W,H))
win.fill((0,0,0))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    for i in range(20000):
        pg.draw.circle(win,BLACK, (random.randint(0,W), random.randint(0,H)),1)
    pressed = pg.mouse.get_pressed()
    if pressed[0]:
        pos = pg.mouse.get_pos()
        pg.draw.circle(win, RED, pos, 50)
    pg.display.update()
    pg.time.delay(20)

    pressed = pg.mouse.get_pressed()
    if pressed[2]:
        pos = pg.mouse.get_pos()
        pg.draw.rect(win, RED, (pos,pos) , 5,5)
