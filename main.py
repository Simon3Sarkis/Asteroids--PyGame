import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock =pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")

    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid = Asteroid(100, 100, 30)
    asteroid.velocity = pygame.Vector2(100, 60) 
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
            
        updatable.update(dt)
        asteroid_field.update(dt)
        for asteroid1 in asteroids:  
            if player.collision(asteroid1):  
                print("Game Over")
                pygame.quit()
                exit()
        for asteroid1 in asteroids:
            for shot1 in shots:
                if shot1.collision(asteroid1):
                    shot1.kill()
                    asteroid1.kill()
                    asteroid1.split()
                    break
        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000

        
if __name__ == "__main__":
    main()