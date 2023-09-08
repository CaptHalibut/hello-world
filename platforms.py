import pygame as pg
from constants import *

class Platform(pg.sprite.Sprite):

    def __init__(self, dimensions, color): 
        super().__init__()
        self.image = pg.Surface((dimensions))
        self.image.fill(color)
        self.rect = self.image.get_rect()
