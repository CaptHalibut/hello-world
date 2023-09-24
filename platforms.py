import pygame as pg
from constants import *

class Platform(pg.sprite.Sprite):

    def __init__(self, dimensions): 
        super().__init__()
        self.image = pg.Surface((dimensions))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

class Ground(pg.sprite.Sprite):

    def __init__(self, dimensions): 
        super().__init__()
        self.image = pg.Surface((dimensions))
        self.image.fill(GREEN_GRASS)
        self.rect = self.image.get_rect()

class NormalPlatform(Platform):

    def __init__(self):
        super().__init__((50,20))
        self.image.fill(BROWN)

class ThickPlatform(Platform):

    def __init__(self): 
        super().__init__((50,40))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()