import pygame as pg
from constants import *
from platforms import *
from crates import *
class Level(object): 

    def __init__(self, player):
        self.platform_list = pg.sprite.Group()
        self.player = player
        self.world_shift = 0
        self.background = None
            
    def update(self):
        self.platform_list.update()

    def draw(self, screen):
        screen.fill(BLUE_SKY)
        self.platform_list.draw(screen)

    def shift_world(self, shift_x):
        self.world_shift += shift_x
        for platform in self.platform_list:
            platform.rect.x += shift_x
      
        
#First Level Platforms and Crates

class Level_01 (Level):

    def __init__(self, player): 
        Level.__init__(self, player)

        self.level_boundary = -1000

        # level_platforms = [((SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2), SMALL_PLATFORM_SIZE, BROWN), ((500, 200), LARGE_PLATFORM_SIZE, GREEN_GRASS), ((1000, 600), THICK_PLATFORM_SIZE, BROWN)]
        
        level__TEST_platforms = [((960, 20), (0, 580), GREEN_GRASS), ((220, 20), (180, 500), BROWN) ]

        # for item in level_platforms: 
        #     platform = Platform(item[0], item[2])
        #     platform.rect.x = item[0][0]
        #     platform.rect.y = item[0][1]
        #     self.platform_list.add(platform)
        
        for item in level__TEST_platforms:
            platform = Platform(item[0], item[2])
            platform.rect.x = item[1][0]
            platform.rect.y = item[1][1]
            self.platform_list.add(platform)
        
        #Add Enemy List
        #Add Background
        #Add crate list

#TODO - Create Level 2
 

#TODO - Create Level 3
#TODO - Create Level 4
#TODO - Create Level 5

