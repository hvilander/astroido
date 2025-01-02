import pygame
from constants import *
from player import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clk = pygame.time.Clock()
    dt = 0

    drawable = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    Player.containers = (drawable, updateable)



    px = SCREEN_WIDTH / 2
    py = SCREEN_HEIGHT / 2
    p = Player(px, py)


    while True:
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for e in updateable:
            e.update(dt)

        for e in drawable:
            e.draw(screen)



        pygame.display.flip()
        dt = clk.tick(60) / 1000



if __name__ == "__main__":
    main()

