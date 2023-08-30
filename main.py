import pygame as pg #Pygame library
from constants import * #Constants file
from player import Player #Player class

#Initialize pygame
pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((BLUE_SKY))
pg.display.set_caption("Platformer")

#Sprite Group - Stores the sprites for the game
current_sprites = pg.sprite.Group()

#Game Loop Flag
endgame = False

#Clock
clock = pg.time.Clock()

#Initialize player
player1 = Player()
player1.rect.x = SCREEN_WIDTH / 2 
player1.rect.y = SCREEN_HEIGHT - player1.rect.height
current_sprites.add(player1)

#Initialize Levels
#TODO - Add level class

#Game loop
while not endgame:

    #Event Handler
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print("Game exited normally.")
            pg.quit()
            exit()
        

        
    pg.display.update()