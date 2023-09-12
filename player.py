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

        self.jump_count = 0
        self.on_wallR = False
        self.on_wallL = False
        self.has_doublejump = False
        self.has_walljump = True
        self.has_sprint = False
        self.lshift = False
    
    #Update player position on the screen
    def update(self):
        self.gravity()

        #Move Character Horizontally
        self.rect.x += self.dx 

        #Check for collision after moving 
        collision_list = pg.sprite.spritecollide(self, self.level.platform_list, False)
        for block in collision_list:
            if self.dx > 0:
                self.rect.right = block.rect.left
                self.on_wallR = True
                self.on_wallL = False
            elif self.dx < 0:
                self.rect.left = block.rect.right
                self.on_wallL = True
                self.on_wallR = False
        if len(collision_list) == 0:
            self.on_wallL = False
            self.on_wallR = False
            #self.dy = 0

        #Move Character Vertically
        self.rect.y += self.dy

        #Check for collision after moving
        collision_list = pg.sprite.spritecollide(self, self.level.platform_list, False)
        for block in collision_list:
            if self.dy > 0:
                self.rect.bottom = block.rect.top
                self.jump_count = 0 #Reset jump on platform
            elif self.dy < 0:
                self.rect.top = block.rect.bottom

    #See if the player is on the ground   
    def on_ground(self):
        self.rect.y += 2
        collision_list = pg.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2        
        if len(collision_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
             return True
        else:
            return False
    
    #Player Gravity
    def gravity(self):
        if self.dy == 0:
            self.dy = 0.7
        elif self.dy < 12:
            self.dy += 0.35

        #Check if player is on the ground

        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.dy >= 0:
            self.dy = 0
            
            #self.rect.y = SCREEN_HEIGHT - self.rect.height
            #Reset jump_count on ground
            
    #Allows player to jump
    def jump(self):
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.jump_count = 0
        if self.has_doublejump == True:
            jump_max = 1
        else:
            jump_max = 0

        #Wall jump test
        if self.has_walljump == True and not self.on_ground() and (self.on_wallL or self.on_wallR):
            if self.on_wallL == True:
                self.dy = -10
                self.dx = 6
                self.on_wallL = False

            elif self.on_wallR == True:
                self.dy = -10
                self.dx = -6
                self.on_wallR = False

        elif self.on_ground() or self.jump_count < jump_max:
            self.dy = -12
            self.jump_count += 1
        
         #elif self.rect.bottom >- SCREEN_HEIGHT:
         #    self.dy = -12
              

    #Player Movement
    #Add time limit to sprint
    def move_left(self):
        if self.lshift == True and self.has_sprint:
            self.dx = -12
        else:
            self.dx = -6
    
    def move_right(self):
        if self.lshift == True and self.has_sprint:
            self.dx = 12
        else:
            self.dx = 6
    
    def stop(self):
        if not self.on_ground():
            if self.dx < 0:
                self.dx += 0.1
            elif self.dx > 0:
                self.dx -= 0.1
        elif self.dx < 0:
            self.dx += 0.5
        elif self.dx > 0:
            self.dx -= 0.5

        