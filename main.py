import pygame
from constants import *
from player import Player 
from asteroid import *
from shot import *
from asteroidfield import *


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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, drawable, updateable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (updateable, drawable, shots)
    

    px = SCREEN_WIDTH / 2
    py = SCREEN_HEIGHT / 2
    p = Player(px, py)
    af = AsteroidField()

    while True:
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        updateable.update(dt)

        for a in asteroids:
            if a.did_hit(p):
                print("GAME OVER")
                return 


        for e in drawable:
            e.draw(screen)


        pygame.display.flip()
        dt = clk.tick(60) / 1000



if __name__ == "__main__":
    main()

