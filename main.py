import pygame as pg #Pygame library
from constants import * #Constants file
from player import Player #Player class
from level import Level #Level class


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

    #Game Loop Flag
    endgame = False

    #Clock
    clock = pg.time.Clock()

    #Initialize player
    player1 = Player()
    player1.rect.x = SCREEN_WIDTH / 2 
    player1.rect.y = SCREEN_HEIGHT - player1.rect.height
    current_sprites.add(player1)

    #Initialize Levels
    #TODO - Import Levels and create levels

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
                if event.key == pg.K_D:
                    player1.move_left()
                if event.key == pg.K_A:
                    player1.move_right()
                if event.key == pg.K_SPACE:
                    player1.jump()


            if event.type == pg.KEYUP:
                if event.key == pg.K_A and player1.dx < 0:
                    player1.stop()
                if event.key == pg.K_D and player1.dx > 0:
                    player1.stop()

        #Update and Draw Sprites
        clear_trail()
        current_sprites.update()
        current_sprites.draw(screen)

        #Update Display
        pg.display.update()

        #Clock Tick
        clock.tick(FPS)

    #Quit Pygame
    pg.quit()

#find and run main
if __name__ == "__main__":
    main()