import pygame as pg


WIN_LENGTH = 800
WIN_HEIGHT = 600

pg.init()

screen = pg.display.set_mode((WIN_LENGTH, WIN_HEIGHT))
screen.fill((0, 0, 0))

pg.display.set_caption("Platformer")

while True:


    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    pg.display.update()