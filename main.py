import sys
import pygame
from constants import *
from logger import log_state, log_event
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Creating Groups and Adding our Object Classes to these containers so we can call and update them at the same time.
    # 2 empty groups called updatable and drawable
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # empty group for asteroids
    asteroids = pygame.sprite.Group()
    # Groups for shots
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)
    
    # Adding asteroid class to the groups
    # This ensures that every instance of the Asteroid class is automatically added o these groups upon creation.
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)   # it is not drawable and it is not an asteroid itself.
    asteroid_field = AsteroidField()
    # Adding Player class to the updatable and drawable groups before player object instance is created.
    Player.containers = (updatable, drawable)
    # We added All future instances of Player class to these containers (groups). 
    # Player instance'i olusturduk bu instance updatable ve drawable grouplari icinde oldugu icin
    # player'i direkt olarak cagirmamiza gerek yok updatable ve drawable cagirarak player'i cagirmis olucaz ve diger class objelerimizi de ayni sekil de.
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)    
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        # player.draw(screen)      Loop over all "drawables" and .draw() them individually. burda da Asteroid class objelerini de cagiricak.
        for drawable_object in drawable:
            drawable_object.draw(screen)
        pygame.display.flip()
        
        # player.update(dt)     Use the new groups instead of the Player object directly. # Asteroid class objelerini de burda cagiricak. Cunku onlari da updatable grubuna dahil ettik.
        updatable.update(dt)
        
        # Iterate over all the objects in asteroids group to check if any of them collide with the player object.
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()
                    # The kill() method is built-in feature of pygame sprites. 
                    # It removes the "killed" object from all of its groups so that the engine stops updating and drawing it.
                    
                
                
                
        # End of each iteration of the game loop
        # It will pause the game loop until 1/60th of a second has passed.
        dt = clock.tick(60) / 1000  # convert from miliseconds to seconds.
        # print(dt)
if __name__ == "__main__":
    main()
