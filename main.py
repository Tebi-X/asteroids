# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
clock = pygame.time.Clock()

#additional files
from constants import *

#import player module
from player import *

def main():
    pygame.init()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Start player object at the middle of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    #Create groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    #Create player and set its containers
    Player.containers = (updatables, drawables)
    player = Player(x, y)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill((0, 0, 0))

        for object in updatables:
            object.update(dt)

        for object in drawables:
            object.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

