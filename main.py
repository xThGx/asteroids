from dataclasses import field

import pygame
from constants import PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH, LINE_WIDTH, PLAYER_TURN_SPEED
from logger import log_state
from player import Player
from asteroid import Asteroid 
from asteroidfield import AsteroidField
import player


def main():
    print("Starting Asteroids with pygame version: ", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    
    # Initialize sprite groups and set containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.container = (updatable,)

    field = AsteroidField()

    dt = 0

    updatable.add(player)
    drawable.add(player)
    updatable.add(asteroids)
    updatable.add(field)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
                
        screen.fill("black")

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time in seconds
       
        #print(f"Delta time: {dt:.4f} seconds")
        #print(f"Updatable count: {len(updatable)}")

if __name__ == "__main__":
    main()  
