import pygame as pg #import pygame library
from constants import * #import constants file

class Player(pg.sprite.Sprite):

    def __init__(self): 
        super().__init__()

        #Attributes
        width = 20
        height = 40

        self.image = pg.Surface([width, height])
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()

        self.dx = 0
        self.dy = 0

        self.level = None
    
    #Update player position
    def update(self):
        #Move Character Horizontally
        self.rect.x += self.dx 

        #Check for collisions
        #TODO - Add collision detection

        #Move Character Vertically
        self.rect.y += self.dy

        #Check for Gravity
        #TODO - Add gravity

    #Allows player to jump
    def jump(self):
        self.rect.y += 3
        self.rect.y -= 3

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.dy = -40
    
    #Player Movement
    def move_left(self):
        self.dx = -6
    
    def move_right(self):
        self.dx = 6
    
    def stop(self):
        self.dx = 0
        