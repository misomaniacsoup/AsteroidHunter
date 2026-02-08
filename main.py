import sys
import pygame
from logger import log_state
from logger import log_event
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for object in updatable:
            object.update(dt)
        for object in asteroids:
            if player.collides_with(object):
                log_event("player_hit")
                print("Game Over!")
                sys.exit(.)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        log_state()

if __name__ == "__main__":
    main()
