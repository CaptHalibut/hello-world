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
        self.level_boundaryL = 0
        self.level_boundaryR = 800
            
    def update(self):
        self.platform_list.update()

    def draw(self, screen):
        screen.fill(BLUE_SKY)
        self.platform_list.draw(screen)

    def shift_world(self, shift_x):

    # Ensure that the camera's horizontal movement is limited within the level boundaries
        if self.level_boundaryL <= self.world_shift + shift_x <= self.level_boundaryR:
            self.world_shift += shift_x
            for platform in self.platform_list:
                platform.rect.x += shift_x
       
        print("Updated world shift: " + str(self.world_shift))
    
#First Level Platforms and Crates

class Level_01 (Level):

    def __init__(self, player): 
        Level.__init__(self, player)

        #Level Boundary
        self.level_boundaryL = 0
        self.level_bouundaryR = 1800

        #List of Platforms and Ground in the Level
        new_paltform_list = [((0,SCREEN_HEIGHT-20), "ground"), ((180,500), "normal"),((300, 500), "thick")]
        ground_list = [((0,SCREEN_HEIGHT-20), "ground", (SCREEN_WIDTH, 20))]

        #Generate Platforms
        for item in new_paltform_list:
            
            if item[1] == "normal":
                platform = NormalPlatform()
                platform.rect.x = item[0][0]
                platform.rect.y = item[0][1]
                self.platform_list.add(platform)
            elif item[1] == "thick":
                platform = ThickPlatform()
                platform.rect.x = item[0][0]
                platform.rect.y = item[0][1]
                self.platform_list.add(platform)
        
        #Generate Terrain
        for item in ground_list: 
            if item[1] == "ground":
                platform = Ground(item[2])
                platform.rect.x = item[0][0]
                platform.rect.y = item[0][1]
                self.platform_list.add(platform)

        #Left Boundary
        platform = Platform((5, SCREEN_HEIGHT))
        platform.rect.x = 0
        platform.rect.y = 0
        self.platform_list.add(platform)
        
        #Add Enemy List
        #Add Background
        #Add crate list