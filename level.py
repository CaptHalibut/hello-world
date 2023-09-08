import pygame as pg
from constants import *
from platforms import *
from crates import *
class Level(object): 

    def __init__(self, player):
        self.player = player
        self.world_shift = 0
        self.background = None
    
    def update(self):
        self.platform_list.update()
        self.crate_list.update()

    def draw(self, screen):
        screen.fill(BLUE_SKY)
        self.platform_list.draw(screen)
        self.crate_list.draw(screen)

    def shift_world(self, shift_x):
        self.world_shift += shift_x
        for platform in self.platform_list:
            platform.rect.x += shift_x
        for crate in self.crate_list:
            crate.rect.x += shift_x
        
#First Level Platforms and Crates

class Level_01 (Level):

    def __init__(self, player): 
        Level.__init__(self, player)

        self.level_boundary = -1000

        level_platforms = [((SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2), SMALL_PLATFORM_SIZE, BROWN), (500, 200, LARGE_PLATFORM_SIZE, GREEN_GRASS), (1000, 600, THICK_PLATFORM_SIZE, BROWN)]

        level_boxes = [((100, 100), GENERIC_BOX_SIZE, BROWN)]

        for item in level_platforms: 
            for characteristic in item:
                platform = Platform(characteristic[2], characteristic[3])
                platform.rect.x = characteristic[0[0]]
                platform.rect.y = characteristic[0[1]]
            self.platform_list.add(platform)
        
        for item in level_boxes:
            box = Crate("box")
            box.rect.x = item[0[0]]
            box.rect.y = item[0[1]]
            self.crate_list.add(box)
        
        #Add Enemy List
    

#TODO - Create Level 2
#TODO - Create Level 3
#TODO - Create Level 4
#TODO - Create Level 5

