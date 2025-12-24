import pygame
from constants import *
from logger import log_state

def main():
    print("Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        pygame.display.flip()

        
        # End of each iteration of the game loop
        # It will pause the game loop until 1/60th of a second has passed.
        dt = clock.tick(60) / 1000  # convert from miliseconds to seconds.
        print(dt)
if __name__ == "__main__":
    main()
