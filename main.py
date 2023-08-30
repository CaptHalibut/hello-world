import pygame as pg #Pygame library
import constants #Constants file

#Initialize pygame
pg.init()
screen = pg.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
screen.fill((constants.BLUE_SKY))
pg.display.set_caption("Platformer")

#Game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    pg.display.update()