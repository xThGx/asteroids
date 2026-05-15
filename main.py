import sys
from tkinter import font

import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS, LINE_WIDTH, PLAYER_SPEED, PLAYER_TURN_SPEED
from logger import log_event, log_state
from player import Player
from shot import Shot


def draw_ui(screen, score, font):
    # .render(text, antialias, color)
    # antialias=True makes the edges smooth
    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    
    # Position the text at (x=20, y=20)
    screen.blit(score_surface, (20, 20))


def main():
    print("Starting Asteroids with pygame version: ", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    original_image = pygame.image.load('Starfield.webp').convert_alpha()
    scaled_image = pygame.transform.scale(original_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    
    # Initialize sprite groups and set containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.container = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    field = AsteroidField()

    dt = 0

    updatable.add(player)
    drawable.add(player)
    updatable.add(asteroids)
    updatable.add(field)
    updatable.add(shots)

    score = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                scaled_image = pygame.transform.scale(original_image, (event.w, event.h))

        updatable.update(dt)
        player.cool_down -= dt

        for asteroid in asteroids:
            #print(f"{player.collides_with(asteroid)}")
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
                return

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    new_asteroids = asteroid.split()
                    shot.kill()
                    score += 1
                    for new_asteroid in new_asteroids:
                        updatable.add(new_asteroid)
                        drawable.add(new_asteroid)
        
        screen.blit(scaled_image, (0, 0))        

        for object in drawable:
            object.draw(screen)

        draw_ui(screen, score, font)
        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time in seconds
       
        #print(f"Delta time: {dt:.4f} seconds")
        #print(f"Updatable count: {len(updatable)}")

if __name__ == "__main__":
    main()  
