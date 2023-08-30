import pygame as pg #Pygame library
from constants import * #Constants file
from player import Player #Player class

def main():
    #Initialize pygame
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((BLUE_SKY))
    pg.display.set_caption("Platformer")

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
    #TODO - Add level class

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
                if event.key == pg.K_LEFT:
                    player1.move_left()
                if event.key == pg.K_RIGHT:
                    player1.move_right()
                if event.key == pg.K_UP:
                    player1.jump()

            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT and player1.dx < 0:
                    player1.stop()
                if event.key == pg.K_RIGHT and player1.dx > 0:
                    player1.stop()

        #Update and Draw Sprites
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