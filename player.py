import pygame as pg #import pygame library
from constants import * #import constants file
from crates import Crate

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

        self.initplayerDisplay()

        #Player life
        self.isAlive = True

        #Movement Attributes
        self.counter = 0
        self.jumpCount = 0
        self.onWallR = False
        self.onWallL = False
        self.hasDoubleJump = False
        self.hasWallJump = False
        self.hasSprint = False
        self.lShift = False
    
    #Update player position on the screen
    def update(self):
        self.updateDisplay()
        self.deathState()
        self.gravity()
        #Move Character Horizontally
        self.rect.x += self.dx 
        #Check for collision after moving 
        collision_list = pg.sprite.spritecollide(self, self.level.platform_list, False)
        self.checkXCollision(collision_list)
        collision_list = pg.sprite.spritecollide(self, self.crates, False)
        self.checkXCollision(collision_list)

        #Move Character Vertically
        self.rect.y += self.dy
        #Check for vertical collision after moving
        collision_list = pg.sprite.spritecollide(self, self.level.platform_list, False)
        self.checkYCollision(collision_list)
        collision_list = pg.sprite.spritecollide(self, self.crates, False)
        self.checkYCollision(collision_list)


        #Check if we hit the screen height
        if self.rect.y == SCREEN_HEIGHT - self.rect.height:
            self.isAlive = False

    def checkXCollision(self, collision_list):
        for block in collision_list:
            if self.dx > 0:
                self.dx = 0
                self.rect.right = block.rect.left
            elif self.dx < 0:
                self.dx = 0
                self.rect.left = block.rect.right


    def checkYCollision(self, collision_list):
        for block in collision_list:
            if self.dy > 0:
                self.rect.bottom = block.rect.top
                self.jumpCount = 0 #Reset jump on platform
            elif self.dy < 0:
                self.rect.top = block.rect.bottom
                self.dy = 0
                if isinstance(block, Crate) and block.broken == False:
                    block.broken = True
                    block.image.fill(RED)
                    self.counter += 1
    
    #See if the player is on the ground   
    def onGround(self):
        self.rect.y += 2
        collision_list = pg.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2        
        for block in collision_list:
            if self.rect.bottom >= block.rect.top:
                return True
                break
            else:
                return False
    
    def deathState(self):
        if self.isAlive == False:
            self.image.fill(RED)
            print("Game Over")
            self.dx = 0
            self.dy = 0

    #Player Gravity
    def gravity(self):
        if self.dy == 0:
            self.dy = 0.7
        elif self.dy < 12:
            self.dy += 0.35

        #Check if player is on the ground

        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.dy >= 0:
            self.dy = 0
            
    #Allows player to jump
    def jump(self):
        if self.onGround():
            self.jumpCount = 0
        else:
            self.jumpCount += 1
        if self.hasDoubleJump == True:
            jumpMax = 1
        else:
            jumpMax = 0

        #Wall jump test
        
        # if self.hasWallJump == True and not self.onGround() and (self.onWallL or self.onWallR):
        #     if self.on_wallL == True:
        #         self.dy = -10
        #         self.dx = 6
        #         self.onWallL = False

        #     elif self.onWallR == True:
        #         self.dy = -10
        #         self.dx = -6
        #         self.onWallR = False

        if self.onGround() or self.jumpCount <= jumpMax:
            self.dy = -12
            
    #Player Movement
    #Add time limit to sprint
    def move_left(self):
        if self.lShift == True and self.hasSprint:
            self.dx = -12
        else:
            self.dx = -6
    
    def move_right(self):
        if self.lShift == True and self.hasSprint:
            self.dx = 12
        else:
            self.dx = 6
    
    def stop(self):
        if self.onGround():
            if self.dx < 0:
                self.dx = round(self.dx)
                self.dx += 1
            elif self.dx > 0:
                self.dx = round(self.dx)
                self.dx -= 1
        elif not self.onGround():
            if self.dx < 0:
                self.dx += 0.1
            elif self.dx > 0:
                self.dx -= 0.1

    def initplayerDisplay(self):
        self.font = pg.font.Font('freesansbold.ttf', 20)
        self.text = self.font.render('', True, WHITE, BLUE_SKY)
        self.textRect = self.text.get_rect()
        self.textRect.x = 10
        self.textRect.y = 10

    def updateDisplay(self):
        self.text = self.font.render(f'Text Here \n Concussions {self.counter}', True, WHITE, BLUE_SKY)