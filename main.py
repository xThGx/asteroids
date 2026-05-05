import pygame
from constants import PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH, LINE_WIDTH, PLAYER_TURN_SPEED
from logger import log_state
from player import Player


def main():
    print("Starting Asteroids with pygame version: ", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    
    while True:
        log_state()
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt)   
        player.draw(screen) 

        pygame.display.flip()

        dt = pygame.time.Clock().tick(60) / 1000  # Limit to 60 FPS and get delta time in seconds
       
        #print(f"Delta time: {dt:.4f} seconds")


if __name__ == "__main__":
    main()  
