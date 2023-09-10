import pygame as pg #Pygame library
from constants import * #Constants file
from player import * #Player class
from level import * #Level class
from crates import * #Crate class

def main():
    #Initialize pygame
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((BLUE_SKY))
    pg.display.set_caption("Platformer")

    def clear_trail():
        screen.fill((BLUE_SKY))

    #Sprite Group - Stores the sprites for the game
    current_sprites = pg.sprite.Group()
    crate_sprites = pg.sprite.Group()

    crate1 = Crate("box")
    crate_sprites.add(crate1)

    #Game Loop Flag
    endgame = False

    #Clock
    clock = pg.time.Clock()

    #Initialize player
    player1 = Player()
    player1.rect.x = 0 
    player1.rect.y = SCREEN_HEIGHT - player1.rect.height
    current_sprites.add(player1)

    #Initialize Levels
    level_list = []
    level_list.append(Level_01(player1))
    current_level = level_list[0]
    player1.level = current_level

    #Game loop
    while not endgame:

        #Event Handler
        for event in pg.event.get():
            if event.type == pg.QUIT:
                print("Game exited normally.")
                pg.quit()
                exit()
            
            #Player Movement Controls
            if event.type == pg.KEYDOWN:
                #Toggle Running
                if event.key == pg.K_LSHIFT:
                    player1.lshift = True
                    if player1.dx < 0:
                        player1.move_left()
                    if player1.dx > 0:
                        player1.move_right()
                #Normal Movement
                if event.key == pg.K_a:
                    player1.move_left()
                if event.key == pg.K_d:
                    player1.move_right() 
                if event.key == pg.K_SPACE:
                    player1.jump()

                #Temporary - flip has_doublejump attribute
                if event.key == pg.K_RSHIFT:
                    print("Double Jump Toggled")
                    player1.has_doublejump = not player1.has_doublejump


            if event.type == pg.KEYUP:
                if event.key == pg.K_LSHIFT:
                    player1.lshift = False
                    if player1.dx < 0:
                        player1.move_left()
                    if player1.dx > 0:
                        player1.move_right()
                if event.key == pg.K_a and player1.dx < 0:
                    player1.stop()
                if event.key == pg.K_d and player1.dx > 0:
                    player1.stop()

        #Update and Draw Sprites
        clear_trail()
        current_sprites.update()
      
        #Scroll Handling
        current_level.update()
        if player1.rect.right >= 500:
            diff = player1.rect.right - 500
            player1.rect.right = 500
            current_level.shift_world(-diff)

        if player1.rect.left <= 120:
            diff = 120 - player1.rect.left
            player1.rect.left = 120
            current_level.shift_world(diff)

        current_level.draw(screen)
        current_sprites.draw(screen)
        crate_sprites.draw(screen)

        #Update Display
        pg.display.update()

        #Clock Tick
        clock.tick(FPS)

    #Quit Pygame
    pg.quit()

#find and run main
if __name__ == "__main__":
    main()