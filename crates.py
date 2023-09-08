import pygame as pg
from constants import *

class Crate(pg.sprite.Sprite):
    def __init__(self, type): 
        super().__init__()

        self.type = type

        #Attributes
        if type == "box":
            
            self.image = pg.Surface(GENERIC_BOX_SIZE)
            self.image.fill(BROWN)
        
        self.rect = self.image.get_rect()
