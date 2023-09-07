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

        #Player Achievements
        self.double_jump_achieved = False
    
    #Update player position on the screen
    def update(self):
        self.gravity()

        #Move Character Horizontally
        self.rect.x += self.dx 

        #Check for collisions
        #TODO - Add collision detection

        #Move Character Vertically
        self.rect.y += self.dy

    #Player Gravity
    def gravity(self):
        if self.dy == 0:
            self.dy = 1
        else:
            self.dy += 0.35

        #Check if player is on the ground
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.dy >= 0:
            self.dy = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    #Allows player to jump
    def jump(self):
        if self.double_jump_achieved == False:

            if self.rect.bottom >= SCREEN_HEIGHT:
                
                self.dy = -8
        
        else
            
            if self.rect.bottom >= SCREEN_HEIGHT:
             self.dy = -8

    
        
    #Player Movement
    def move_left(self):
        self.dx = -6
    
    def move_right(self):
        self.dx = 6
    
    def stop(self):
        self.dx = 0
        